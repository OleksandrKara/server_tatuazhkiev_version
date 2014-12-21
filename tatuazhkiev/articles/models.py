# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=255) # заголовок поста
    datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    short_description = content = models.TextField(max_length=10000) # малый текст поста
    content = HTMLField() # текст поста

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/articles/%i/" % self.id