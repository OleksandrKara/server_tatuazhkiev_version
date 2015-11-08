from django.db import models
from django.contrib.flatpages.models import FlatPage as FlatPageOld

class ExtendedFlatPage(FlatPageOld):
    meta_keywords = models.CharField(max_length=500)
    meta_description = models.CharField(max_length=500)