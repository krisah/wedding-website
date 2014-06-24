from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


# Create your views here.
def home(request):
    template = loader.get_template("index.html")
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def cover(request):
    template = loader.get_template("cover.html")
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))