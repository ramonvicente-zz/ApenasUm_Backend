"""
Django settings for apenas_um project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from decouple import config

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def base_dir_join(*args):
    return os.path.join(BASE_DIR, *args)


APPS_DIR = base_dir_join('apps')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [
    ("""Admin""", 'contato@3ysoftwarehouse.com.br'),
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2i^xo^i&vkg-hg7tssd*eqe4fgcc1me-&8zhwwymtuftvtfuua'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# CSRF_COOKIE_SECURE=False

# Application definition

DJANGO_APPS = [
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
    'django.contrib.admindocs',
]

THIRD_PARTY_APPS = [
    'nested_admin',
]

# Apps specific for this project go here.
LOCAL_APPS = [
    # custom users app
    'apps.api',
    'apps.common',
    'apps.core',
    'apps.client',
    'apps.dashboard',
    'apps.message_core',
    # Your stuff: custom apps go here
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

ROOT_URLCONF = 'apenas_um.urls'

ADMIN_URL = r'^admin/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [base_dir_join('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    },
]

WSGI_APPLICATION = 'apenas_um.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = False

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = str(base_dir_join('staticfiles'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    base_dir_join('static'),
)

# MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(base_dir_join('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

'''
SIMPLE HISTORY
'''

INSTALLED_APPS += ['simple_history', ]

MIDDLEWARE += [
    'simple_history.middleware.HistoryRequestMiddleware',
]

'''
DJANGO REST FRAMEWORK
'''

INSTALLED_APPS += ['rest_framework',
'rest_framework.authtoken',
'rest_auth',
'django_filters',
'rest_framework_swagger',
'oauth2_provider',
'allauth',
'allauth.account',
'allauth.socialaccount',
'allauth.socialaccount.providers.facebook',
'allauth.socialaccount.providers.instagram',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.SearchFilter',
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'PAGE_SIZE': 50
}

LOGIN_REDIRECT_URL = '/dashboard/'
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    },
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
}

ADMIN_SITE_HEADER = "Administração Apenas Um"

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

OAUTH2_PROVIDER = {
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'},
    'ACCESS_TOKEN_EXPIRE_SECONDS': 60 * 60 * 24 * 180,
}

'''
EMAIL
'''

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_FROM = ''

'''
SMS
'''
SMS_FROM = 'PROJETO'
SMS_TOKEN = 'aGlwcm86MmVKTFg0UlZCQg=='
