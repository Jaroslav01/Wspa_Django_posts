from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    # comments = models.ManyToManyField(Comment)

class Comment(models.Model):
    author = models.TextField(default='')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
