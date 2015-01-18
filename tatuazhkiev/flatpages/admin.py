from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from models import ExtendedFlatPage

class ExtendedFlatPageForm(FlatpageForm):
    class Meta:
        model = ExtendedFlatPage

class ExtendedFlatPageAdmin(FlatPageAdmin):
    form = ExtendedFlatPageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'meta_keywords', 'meta_description', 'content', 'sites', 'template_name')}),
    )     

admin.site.unregister(FlatPage)
admin.site.register(ExtendedFlatPage, ExtendedFlatPageAdmin)