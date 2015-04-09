# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.contrib.sitemaps.views import sitemap
from tatuazhkiev.fotos.models import Foto
from django.contrib.flatpages import views

sitemaps = {
    'flatpages': FlatPageSitemap,
}

admin.autodiscover()


urlpatterns = patterns('tatuazhkiev.views',
    (r'^photo/$', 'photo_handler'),
)

#special for index.html
urlpatterns += [
    url(r'^index.html/?$', views.flatpage, {'url': '/'}),
]

urlpatterns += patterns('',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps':sitemaps}),
)

urlpatterns += patterns('',
    (r'^tinymce/', include('tinymce.urls')),
    #(r'^admin/filebrowser/', include(admin.site.urls)),
    (r'^admin/filebrowser/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('tatuazhkiev.fotos.views',
    (r'^kontakti/$', 'kontakti_handler'),
	(r'^contact/$', 'kontakti_handler'),
    (r'^thanks/$', 'thanks'),
	(r'^xhr_test$', 'xhr_test'),
)

urlpatterns += patterns('',
	(r'^articles/', include('tatuazhkiev.articles.urls')),
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()