"""
Django settings for tatuazhkiev project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__)) 
#TEMPLATE_DIRS = ( os.path.join(BASE_DIR, 'templates'), )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '06&(uw0lsobw9(3i@ajnfuf_lm#wbj+v6ph+)!g@7s(+tm84*o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

THUMBNAIL_DEBUG = True

ALLOWED_HOSTS = ['tatuazhkiev.com.ua','127.0.0.1:8000','localhost:8000']

SITE_ID = 2

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'tatuazhkiev.fotos',
	'tatuazhkiev.flatpages',
	'sorl.thumbnail',
	'django.contrib.sitemaps',
	#'django.contrib.flatpages',
	'django.contrib.sites',
	'tinymce',
    'tatuazhkiev.mymenu',
    'tatuazhkiev.articles',
    'disqus',
	'django_evolution',
	'filebrowser',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'tatuazhkiev.mymenu.context_processors.context',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)



ROOT_URLCONF = 'tatuazhkiev.urls'

WSGI_APPLICATION = 'tatuazhkiev.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tatuazhkiev',
		'USER': 'root',
		'PASSWORD': 'TrustPoint85',
		'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
#TEMPLATE_DIRS = os.path.join(PROJECT_PATH, 'templates')
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'),)

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'files', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'files', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

ADMIN_MEDIA_PREFIX = '/static/admin/'
FILEBROWSER_DIRECTORY = 'data/'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'kiev.tatuazh@gmail.com'
EMAIL_HOST_PASSWORD = 'karaanna'

TINYMCE_JS_URL = os.path.join(STATIC_URL, "tiny_mce/tiny_mce.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_URL, "tiny_mce")

DEFAULT_URL_TINYMCE = os.path.join(STATIC_URL, "tiny_mce")
DEFAULT_PATH_TINYMCE = os.path.join(STATIC_URL, "tiny_mce")

TINYMCE_DEFAULT_CONFIG = {
    # custom plugins
    'plugins': "table,spellchecker,paste,searchreplace",
    # editor theme
    'theme': "advanced",
    # custom CSS file for styling editor area
    #'content_css': STATIC_ROOT + "css/custom_tinymce.css",
    # use absolute urls when inserting links/images
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}

#TINYMCE_SPELLCHECKER = True
#TINYMCE_COMPRESSOR = True

DISQUS_API_KEY = 'uYCrQucNzezmexT8uLj2mEA6Rxi1gf2sSqipmmy7wl8t3jtYfL6I4ICeeDozNgEg'
DISQUS_WEBSITE_SHORTNAME = 'tatuazhkiev'
