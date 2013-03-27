from django.db import models
from taggit.managers import TaggableManager


class Post(models.Model):
    """docstring for Post"""
    title = models.CharField(max_length=100)
    perex = models.TextField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __unicode__(self):
        return self.title
