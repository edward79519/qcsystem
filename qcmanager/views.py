from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    template = loader.get_template('qcmanager/index.html')
    context = {}
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
