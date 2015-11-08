# -*- coding: utf-8 -*-
from django.contrib import admin
from tatuazhk.articles.models import Post

class ArticleAdmin(admin.ModelAdmin):
    list_display  = ('__unicode__', 'title', 'get_full_url' )
    ordering      = ('datetime', )
    prepopulated_fields = {"slug": ("title",)}
	
admin.site.register(Post,ArticleAdmin)