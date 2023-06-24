from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Note(models.Model):
    """Model for a single note"""
    title = models.CharField(max_length=200)
    text = models.TextField(default=' ')
    created = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=50)
    comments = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='note')
