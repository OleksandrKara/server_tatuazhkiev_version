# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.contrib.sitemaps.views import sitemap
#from tatuazhk.sitemap import SitemapArticlesXML, StaticViewSitemap
from tatuazhk.fotos.models import Foto
from django.contrib.flatpages import views

sitemaps = {
    'flatpages': FlatPageSitemap,
    #'articles': SitemapArticlesXML,
    #'static': StaticViewSitemap,
}


admin.autodiscover()


urlpatterns = patterns('tatuazhk.views',
    (r'^photo/$', 'photo_handler'),
)

#special for index.html
urlpatterns += [
    url(r'^index.html/?$', views.flatpage, {'url': '/'}),
]

urlpatterns += patterns('',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps':sitemaps}),
    #(r'^sitemap2\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps':SitemapArticlesXML}),
    #url(r'^$', 'main_blog.views.index', name='index'),
)

urlpatterns += patterns('',
    (r'^admin/',  include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
)

urlpatterns += patterns('tatuazhk.fotos.views',
    (r'^kontakti/$', 'kontakti_handler'),
	(r'^contact/$', 'kontakti_handler'),
    (r'^thanks/$', 'thanks'),
	(r'^xhr_test$', 'xhr_test'),
)

urlpatterns += patterns('',
	(r'^articles/', include('tatuazhk.articles.urls')),
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()