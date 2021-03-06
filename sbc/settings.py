# Django settings for sbc project.

import os, base64

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG = os.environ['debug'] == "True"
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Yasyf Mohamedali', 'yasyf@mit.edu'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.environ['db_name'],                      # Or path to database file if using sqlite3.
        'HOST': os.environ['db_host'],
        'USER': os.environ['db_user'],
        'PASSWORD': os.environ['db_pass'],
        'PORT': '',                       # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['mitsbc.mit.edu','mitsbc.herokuapp.com','sbc.scripts.mit.edu','mit-sbc.org','www.mit-sbc.org','localhost','127.0.0.1']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_PATH + '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_PATH + '/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ['sk']

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'sbc.middleware.EnforceHostnameMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'home.middleware.TimezoneMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.core.context_processors.request',
  'django.contrib.auth.context_processors.auth',
)

ROOT_URLCONF = 'sbc.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'sbc.wsgi.application'
TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'suit',
    'tinymce',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south',
    'gunicorn',
    'storages',
    'boto',
    'collectfast',
    'home',
    'drop',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

SUIT_CONFIG = {
    'ADMIN_NAME': 'MIT SBC',
    'MENU': (
        {'app': 'auth', 'label': 'Authorization', 'icon':'icon-lock'},
        '-',
        {'app': 'home', 'label': 'Main Site'},
        {'app': 'drop', 'label': 'INE/Resume Drop'}
    ),
    'HEADER_TIME_FORMAT': 'h:i A'
}

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'theme_advanced_disable' : "help,code,cleanup,anchor,styleselect",
    'theme_advanced_buttons3' : "",
}

STATIC_VERSION = os.getenv('STATIC_VERSION', 1)
GCAL_URL = os.getenv('GCAL_URL')

EMAIL_HOST = os.environ['email_host']
EMAIL_HOST_USER = os.environ['email_user']
EMAIL_HOST_PASSWORD = base64.b64decode(os.environ['email_pass'])
EMAIL_PORT = 587
EMAIL_USE_TLS = True

AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_QUERYSTRING_AUTH = False
AWS_PRELOAD_METADATA = True
AWS_S3_SECURE_URLS = True
AWS_HEADERS = {
    'Cache-Control': 'public, max-age=86400',
    'x-amz-acl': 'public-read',
}
AWS_S3_CUSTOM_DOMAIN = 'd2ssbkyk5x8g9g.cloudfront.net'
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
S3_URL = 'https://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
CF_URL = 'https://%s' % AWS_S3_CUSTOM_DOMAIN

if not DEBUG:
    ENFORCE_HOSTNAME = 'mitsbc.mit.edu'
    DEFAULT_FILE_STORAGE = 'sbc.s3utils.MediaRootS3BotoStorage'
    STATICFILES_STORAGE = 'sbc.s3utils.StaticRootS3BotoStorage'
    STATIC_URL = CF_URL + '/media/'
    MEDIA_URL = CF_URL + '/static/'
    TINYMCE_JS_ROOT = STATIC_URL + "tiny_mce"
    TINYMCE_JS_URL = TINYMCE_JS_ROOT + "/tiny_mce.js"
