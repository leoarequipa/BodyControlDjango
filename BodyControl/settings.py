"""
Django settings for BodyControl project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/

"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import logging
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



SECRET_KEY = 'yyl7a8d6g)04nsen-3*aih*9w0yvu2q+p$ch=gdzmgwla^3f7p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'BodyControl.apps.main',
    'BodyControl.apps.estado',
    'BodyControl.apps.food',
    'BodyControl.apps.day',
    'BodyControl.apps.recommendation',
    #'bootstrapform',
    'crispy_forms',
    'imagekit',
    #'sorl.thumbnail',


)

#TENGO QUE VERLO COMO UNA CEBOLLA, CADA CAPA ENVUELVE A LA OTRA Y SON DEPENDIENTES

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)


ROOT_URLCONF = 'BodyControl.urls'

WSGI_APPLICATION = 'BodyControl.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOGIN_URL = "/users/login/"

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    #'/home/salchicha/Django-Proyectos/Proyecto1/BodyControl/BodyControl/static/',
    os.path.join(BASE_DIR, "BodyControl/static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
TEMPLATE_DIRS = (
       #'/home/salchicha/Django-Proyectos/Proyecto1/BodyControl/BodyControl/templates/',
       os.path.join(BASE_DIR, "BodyControl/templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "BodyControl.apps.main.processor.index",
    "BodyControl.apps.recommendation.processor.recomendation",

)

MEDIA_URL = "/media/"


MEDIA_ROOT = os.path.join(BASE_DIR, "BodyControl/media")
