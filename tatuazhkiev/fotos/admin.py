from django.contrib import admin
from tatuazhkiev.fotos.models import Foto

class FotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'date', 'image_tag')
    search_fields = ('title', 'date','image_tag')

admin.site.register(Foto, FotoAdmin)