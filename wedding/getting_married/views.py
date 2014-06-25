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


def about_us(request):
    template = loader.get_template("about_us.html")
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))


def contact(request):
    template = loader.get_template("contact.html")
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def wedding_event(request):
    template = loader.get_template("wedding_event.html")
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def travel(request):
    template = loader.get_template("travel.html")
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def accommodations(request):
    template = loader.get_template("accommodations.html")
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def registy(request):
    template = loader.get_template("registy.html")
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def photo_album(request):
    template = loader.get_template("photo_album.html")
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def guest_book(request):
    template = loader.get_template("guest_book.html")
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

