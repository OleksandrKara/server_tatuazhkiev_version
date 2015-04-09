# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from tinymce import models as tinymce_models

class Post(models.Model):
    title = models.CharField(max_length=255) # заголовок поста
    slug = models.SlugField('slug', max_length=255,unique_for_date='datetime')
    meta_keywords = models.CharField(max_length=500)
    meta_description = models.CharField(max_length=500)
    datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    short_description = content = models.TextField(max_length=10000) # малый текст поста
    content = tinymce_models.HTMLField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])
		
    def get_full_url(self):
        domain = Site.objects.get_current()
        articleUrl = reverse('detail', args=[self.slug])
        fullUrl = "https://%s%s" % (domain,articleUrl)
        return fullUrl