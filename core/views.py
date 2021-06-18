from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Employee, Land, County, Area, Section
from .forms import EmployeeCreationForm, LoginForm, ChangePWDForm, EmployeeUpdateForm, UserUpdateForm, LandForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.db import transaction, DatabaseError
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.


@login_required
def index(request):
    employee = User.objects.get(id=request.user.id)
    template = loader.get_template('core/index.html')
    context = {
        'employee': employee,
    }
    return HttpResponse(template.render(context, request))


@login_required
@permission_required('auth.add_user', raise_exception=True)
def user_signup(request):
    template = loader.get_template('core/register.html')
    form = EmployeeCreationForm()
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def user_login(request):
    form = LoginForm()
    template = loader.get_template('core/login.html')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get("next"))
                else:
                    return redirect('/')
            else:
                messages.error(request, '使用者尚未啟用，請聯絡管理員。')
                return redirect('/login/')
        else:
            messages.error(request, '使用者帳號或密碼有誤，請再次輸入。')
            return redirect('/login/')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


def user_logout(request):
    logout(request)
    return redirect('/')


@login_required
def user_change_pwd(request):
    template = loader.get_template('core/change_password.html')
    if request.method == 'POST':
        form = ChangePWDForm(request.user, request.POST)
        # form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "修改密碼成功！")
            return HttpResponseRedirect('../')
        else:
            print(form.errors)
            messages.error(request, "有哪裡出錯，請再試一次！")
            return HttpResponseRedirect('./')
    else:
        form = ChangePWDForm(request.user)
        # form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def user_update_profile(request):
    template = loader.get_template('core/editprof.html')
    user = User.objects.get(username=request.user.username)
    user_prof = Employee.objects.get(user=user)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        prof_form = EmployeeUpdateForm(request.POST, instance=user_prof)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save(commit=False)
            prof_form.user = user
            prof_form.save()
            return HttpResponseRedirect('../')
    else:
        user_form = UserUpdateForm(instance=user)
        prof_form = EmployeeUpdateForm(instance=user_prof)
    context = {
        'user_form': user_form,
        'prof_form': prof_form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def land_add(request):
    template = loader.get_template('core/land/addland.html')
    if request.method == "POST":
        form = LandForm(request.POST)
        if form.is_valid():
            print(form.is_valid())
            try:
                with transaction.atomic():
                    county, county_created = County.objects.get_or_create(
                        sn=form.cleaned_data['county'],
                        name=request.POST['county_ch'],
                    )
                    area, area_created = Area.objects.get_or_create(
                        sn=form.cleaned_data['area'],
                        county=county,
                        name=request.POST['area_ch'])
                    section, sec_created = Section.objects.get_or_create(
                        sn=form.cleaned_data['section'],
                        area=area,
                        office=form.cleaned_data['office'],
                        name=request.POST['section_ch'],
                    )
                    land, land_created = Land.objects.get_or_create(
                        sn=form.cleaned_data['locnum'],
                        section=section,
                        cx=form.cleaned_data['cx'],
                        cy=form.cleaned_data['cy'],
                        lx=form.cleaned_data['lx'],
                        ly=form.cleaned_data['ly'],
                        rx=form.cleaned_data['rx'],
                        ry=form.cleaned_data['ry'],
                    )
                if land_created:
                    messages.success(request, "成功新增一筆土地：{}-{}。".format(land.section.name, land.sn))
                    return HttpResponseRedirect("/core/land/")
                else:
                    messages.error(request, "此土地已新增，請輸入下一筆。")
                    return HttpResponseRedirect("./")
            except DatabaseError as e:
                print(e)
                messages.error(request, "新增錯誤，請再確認輸入內容。")
                return HttpResponseRedirect("./")
        else:
            messages.error(request, "新增錯誤，請再確認輸入內容。")
            print(form.is_valid())
            return HttpResponseRedirect("./")
    else:
        form = LandForm()
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def land_list(request):
    template = loader.get_template("core/land/landlist.html")
    lands = Land.objects.all()
    context = {
        'lands': lands,
    }
    return HttpResponse(template.render(context, request))
