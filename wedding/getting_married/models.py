from django.db import models

# Create your models here.

class Guest(models.Model):
    user = models.CharField(max_length=200)

class Comment(models.Model):
    guest = models.ForeignKey(Guest)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
