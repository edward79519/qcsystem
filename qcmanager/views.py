from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Project, ProjCategory, SlfChkStandIn
# Create your views here.


@login_required
def index(request):
    template = loader.get_template('qcmanager/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


@login_required
def project(request):
    template = loader.get_template('qcmanager/project/proj_list.html')
    proj = Project.objects.all()
    context = {
        'projs': proj,
    }
    return HttpResponse(template.render(context, request))


@login_required
def proj_detail(request, p_id):
    template = loader.get_template('qcmanager/project/detail.html')
    proj = Project.objects.get(id=p_id)
    cate_list = ProjCategory.objects.filter(cproj_id=p_id)
    context = {
        'proj': proj,
        'cate_list': cate_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def cate_detail(request, cate_id):
    template = loader.get_template('qcmanager/category/detail.html')
    cate = ProjCategory.objects.get(id=cate_id)
    context = {
        'cate': cate,
    }
    return HttpResponse(template.render(context, request))


@login_required
def slfchkstandin_detail(request, chk_id):
    template = loader.get_template('qcmanager/selfcheck/SlfChkStandIn_Detail.html')
    standin = SlfChkStandIn.objects.get(id=chk_id)
    context = {
        'standin': standin,
    }
    return HttpResponse(template.render(context, request))


def category(request):
    template = loader.get_template('qcmanager/category/list.html')
    context = {}
    return HttpResponse(template.render(context, request))


def works(request):
    template = loader.get_template('qcmanager/works/list.html')
    context = {}
    return HttpResponse(template.render(context, request))


def arng(request):
    template = loader.get_template('qcmanager/arrange/list.html')
    context = {}
    return HttpResponse(template.render(context, request))


def arng_add(request):
    template = loader.get_template('qcmanager/arrange/add.html')
    context = {}
    return HttpResponse(template.render(context, request))
