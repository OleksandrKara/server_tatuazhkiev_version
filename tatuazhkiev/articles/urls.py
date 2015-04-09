#coding: utf-8
from django.conf.urls import patterns, url
from tatuazhkiev.articles.views import PostsListView, PostDetailView 

urlpatterns = patterns('',
url(r'^$', PostsListView.as_view(), name='list'),
url(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='detail'),
)