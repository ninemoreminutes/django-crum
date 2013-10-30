# Python
import os
import sys

# Django
from django.conf import global_settings

# Update this module's local settings from the global settings module.
this_module = sys.modules[__name__]
for setting in dir(global_settings):
    if setting == setting.upper():
        setattr(this_module, setting, getattr(global_settings, setting))

# Absolute path to the directory containing this Django project.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test_project.sqlite3'),
    }
}

TIME_ZONE = 'America/New_York'

USE_TZ = True

SITE_ID = 1

SECRET_KEY = '347e28aa55547c3195e028fdead3448817e74fe2'

STATICFILES_DIRS = ()

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'media')

MIDDLEWARE_CLASSES += (
    'crum.CurrentRequestUserMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

ROOT_URLCONF = 'test_project.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'rest_framework',
    'test_app',
)

try:
    import django_extensions
    INSTALLED_APPS += ('django_extensions',)
except ImportError:
    pass

try:
    import debug_toolbar
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
except ImportError:
    pass

try:
    import devserver
    INSTALLED_APPS += ('devserver',)
except ImportError:
    pass

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

DEVSERVER_DEFAULT_ADDR = '127.0.0.1'
DEVSERVER_DEFAULT_PORT = '8034'

TEST_RUNNER = 'hotrunner.HotRunner'

EXCLUDED_TEST_APPS = [x for x in INSTALLED_APPS if x != 'test_app']
