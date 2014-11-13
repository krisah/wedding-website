from django import forms
from django.db import models
#from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
# Create your models here.

class Comment(models.Model):
    guest = models.TextField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class ContactForm(forms.Form):
    name = forms.CharField()
    from_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
