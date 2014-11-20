# -*- coding: utf-8 -*-
# Импортируем базовый класс
from django.contrib.sitemaps import Sitemap
# Импортируем модель с данными 
#from fotos.models import Foto

'''class SitemapXML(Sitemap):
    # Частота обновления страницы (см. http://www.sitemaps.org/) 
    changefreq = 'weekly'
    # Приоритет сканирования страницы (см. http://www.sitemaps.org/)
    priority = 0.5

    def items(self):
        # Выбираем из источника данных те данные для которых необходимо
        # построить файл sitemap
        return Foto.objects.filter(date__lte='2055-01-01').order_by('id')
		#date__lte='2055-01-01'

    def lastmod(self, obj):
        # Метод возвращает дату которая указывается в параметре lastmod
        # (см. http://www.sitemaps.org/)
        return obj.date

    def location(self, obj):
        # Метод возвращает URL который указывается в параметре loc
        # (см. http://www.sitemaps.org/)
        return "/media/%s" % obj.image_location'''
		
class FlatpageSitemap(Sitemap): 
    def items(self): 
        from django.contrib.sites.models import Site 
        return FlatPage.all().filter('sites = ', 
Site.objects.get_current().key()) 