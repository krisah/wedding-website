from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from getting_married.models import *
import json

# Create your views here.
def home(request):
    template = loader.get_template("home.html")
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

@csrf_exempt
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

def registry(request):
    template = loader.get_template("registry.html")
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

def photo_album(request):
    template = loader.get_template("photo_album.html")
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

@csrf_exempt
def guest_book(request):
    template = loader.get_template("guest_book.html")
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

@csrf_exempt
def guest_book_post(request):
    if request.body != "":
        post_dict = json.loads(request.body)
        print("it's a python dict: " + str(post_dict))
        new_comment = Comment(guest=post_dict['guest'],
                              comment=post_dict['comment'])
        new_comment.save()
    comments = []
    for g in Comment.objects.all():
        comments.append({'guest': g.guest, 'comment': g.comment})
    return HttpResponse(json.dumps(comments), mimetype="application/json")

def program(request):
    template = loader.get_template("program.html")
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))
