from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project, Category, WorkList, Question, Choice, AnsSingle, SubCateSelect
from .forms import (ProjectAddForm, ProjectUpdateForm, CateAddForm, CateUpdateForm, WorkListAddForm, WorkListUpdateForm,
                    QuestionAddForm, ChoiceAddForm, Task, TaskAddForm)
from django.db import transaction, DatabaseError


# Create your views here.


def index(request):
    template = loader.get_template("qc/index.html")
    proj_list = Project.objects.all()
    context = {
        'proj_list': proj_list,
    }
    return HttpResponse(template.render(context, request))


def proj_detail(request, proj_id):
    template = loader.get_template("qc/project/detail.html")
    proj = Project.objects.get(id=proj_id)
    cate_list = Category.objects.filter(proj_id=proj_id).order_by('name')
    context = {
        'proj': proj,
        'cate_list': cate_list,
    }
    return HttpResponse(template.render(context, request))


def proj_add(request):
    template = loader.get_template("qc/project/add.html")
    if request.method == 'POST':
        form = ProjectAddForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/qc/')
    else:
        form = ProjectAddForm()
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def proj_update(request, proj_id):
    template = loader.get_template("qc/project/update.html")
    proj = Project.objects.get(id=proj_id)
    if request.method == 'POST':
        form = ProjectUpdateForm(request.POST, instance=proj)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('../')
    else:
        form = ProjectUpdateForm(instance=proj)
    context = {
        'proj': proj,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def cate_detail(request, cate_id):
    template = loader.get_template("qc/category/detail.html")
    cate = Category.objects.get(id=cate_id)
    work_list = WorkList.objects.filter(cate_id=cate_id)
    context = {
        'cate': cate,
        'work_list': work_list,
    }
    return HttpResponse(template.render(context, request))


def cate_add(request, proj_id):
    template = loader.get_template("qc/category/add.html")
    proj = Project.objects.get(id=proj_id)

    if request.method == 'POST':
        form = CateAddForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                    # 讓project資料留存更新者
                    proj.editor = request.user
                    proj.save()
            except DatabaseError as e:
                print(e)
        return HttpResponseRedirect("../")
    else:
        form = CateAddForm(request.POST)
    context = {
        'proj': proj,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def cate_update(request, cate_id):
    template = loader.get_template("qc/category/update.html")
    cate = Category.objects.get(id=cate_id)
    if request.method == 'POST':
        form = CateUpdateForm(request.POST, instance=cate)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                    proj = cate.proj
                    proj.editor = request.user
                    proj.save()
            except DatabaseError as e:
                print(e)
        return HttpResponseRedirect("../")
    else:
        form = CateUpdateForm(instance=cate)
    context = {
        'cate': cate,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def worklist_detail(request, wk_id):
    template = loader.get_template("qc/worklist/detail.html")
    wklst = WorkList.objects.get(id=wk_id)
    quest_list = Question.objects.filter(worklist_id=wk_id).order_by("ordering")
    task_list = Task.objects.filter(worklist_id=wk_id)
    if request.method == "POST":
        form = QuestionAddForm(request.POST, request.FILES)
        taskform = TaskAddForm(request.POST)
        if form.is_valid() and not taskform.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                    wklst.editor = request.user
                    wklst.save()
            except DatabaseError as e:
                print(e)
        elif taskform.is_valid():
            taskform.save()
        else:
            print(form.is_valid())
            print(taskform.is_valid())
        return HttpResponseRedirect("./")
    else:
        taskform = TaskAddForm()
        form = QuestionAddForm()
    context = {
        'wklst': wklst,
        'quest_list': quest_list,
        'task_list': task_list,
        'form': form,
        'taskform': taskform,
    }
    return HttpResponse(template.render(context, request))


def worklist_add(request, cate_id):
    template = loader.get_template("qc/worklist/add.html")
    cate = Category.objects.get(id=cate_id)
    if request.method == "POST":
        form = WorkListAddForm(request.POST)
        form.fields['subcate'].queryset = SubCateSelect.objects.filter(cate__id=cate.name.id)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                    cate.editor = request.user
                    cate.save()
            except DatabaseError as e:
                print(e)
        else:
            print(form.is_valid())
        return HttpResponseRedirect("../")
    else:
        form = WorkListAddForm(request.POST)
        form.fields['subcate'].queryset = SubCateSelect.objects.filter(cate__id=cate.name.id)
    context = {
        'cate': cate,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def worklist_update(request, wk_id):
    template = loader.get_template("qc/worklist/update.html")
    wklst = WorkList.objects.get(id=wk_id)
    if request.method == "POST":
        form = WorkListUpdateForm(request.POST, instance=wklst)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                    cate = wklst.cate
                    cate.editor = request.user
                    cate.save()
            except DatabaseError as e:
                print(e)
            finally:
                return HttpResponseRedirect("../")
        else:
            print(form.is_valid())
            return HttpResponseRedirect("./")
    else:
        form = WorkListUpdateForm(instance=wklst)
    context = {
        'wklst': wklst,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def question_detail(request, quest_id):
    template = loader.get_template("qc/question/list.html")
    question = Question.objects.get(id=quest_id)
    if request.method == "POST":
        form = ChoiceAddForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                    question.editor = request.user
                    question.save()
            except DatabaseError as e:
                print(e)
            finally:
                return HttpResponseRedirect("./")
    else:
        form = ChoiceAddForm(request.POST)
    context = {
        'question': question,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def choice_delete(request, choice_id, quest_id):
    choice = Choice.objects.get(id=choice_id)
    choice.delete()
    return HttpResponseRedirect("/qc/question/{}/".format(str(quest_id)))


def task_fill(request, task_id):
    task = Task.objects.get(id=task_id)
    questions = Question.objects.filter(worklist_id=task.worklist.id)
    template = loader.get_template('qc/task/fill.html')
    if request.method == "POST":
        ans_objs = []
        for key in request.POST:
            if "csrf" not in key:
                q_type = Question.objects.get(id=key).type
                if q_type == 0:
                    ans = AnsSingle(
                        task=task,
                        editor=request.user,
                        question_id=key,
                        choice_id=request.POST[key],
                    )
                    print(ans.task)
                    ans_objs.append(ans)
        print(ans_objs)
        try:
            with transaction.atomic():
                AnsSingle.objects.bulk_create(ans_objs)
                task.is_filled = True
                task.save()
                return HttpResponseRedirect('/qc/worklist/' + str(task.worklist.id) + '/')
        except DatabaseError as e:
            print(e)
            return HttpResponseRedirect('./')
    context = {
        'task': task,
        'questions': questions,
    }
    return HttpResponse(template.render(context, request))


def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    questions = Question.objects.filter(worklist_id=task.worklist.id)
    template = loader.get_template('qc/task/detail.html')
    '''
    ans = {}
    for question in questions:
        if question.type == 0:
            ans[question.id] = AnsSingle.objects.get(task=task, question=question).choice.desc
    '''
    context = {
        'task': task,
        'questions': questions,
    }
    return HttpResponse(template.render(context, request))
