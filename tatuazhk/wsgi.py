"""
WSGI config for tatuazhkiev project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os
import sys
#import site

sys.path.append('/var/www/python/tatuazhkiev/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tatuazhkiev.settings")
#site.addsitedir('/home/arkhangl/python27/lib/python2.7/site-packages')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
