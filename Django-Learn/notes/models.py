from django.db import models

# Create your models here.


class Note(models.Model):
    """Model for a single note"""
    title = models.CharField(max_length=200)
    text = models.TextField(default=' ')
    created = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=50)
    comments = models.TextField(default='')
