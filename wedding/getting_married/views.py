from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from getting_married.models import *
import json
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail, BadHeaderError
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

@csrf_exempt
def contact_email(request):
    name = request.POST.get('name','')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    recipient = ['krisandmarissa5162015@gmail.com']
    if message and from_email and name:
        try:
            send_mail(name, message, from_email, recipient)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/getting_married/thank_you/')
    else:
        return render_to_response('contact.html', {'form': ContactForm()})
                            
    return render_to_response('contact.html', {'form': ContactForm()},
        RequestContext(request))


def thankyou(request):
    return render_to_response('thank_you.html')

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

def thank_you(request):
    template = loader.get_template("thank_you.html")
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))

