from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=32)


class Post(models.Model):
    text = models.TextField()
    headline = models.CharField(max_length=128)
    authors = models.ManyToManyField(User)

    published_on = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag)
