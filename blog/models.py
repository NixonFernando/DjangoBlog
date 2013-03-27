from django.db import models
from taggit.managers import TaggableManager


class Post(models.Model):
    """docstring for Post"""
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    sumario = models.TextField(max_length=400)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __unicode__(self):
        return self.titulo
