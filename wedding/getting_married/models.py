from django.db import models

# Create your models here.

class Comment(models.Model):
    guest = models.TextField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


