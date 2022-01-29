"""
Django settings for denarios project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os, sys
import django_heroku
from pathlib import Path
from decouple import config
from dj_database_url import parse as dburl
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-305n6d$)+$wuri=^52**!%xwk_+9aax*n6t-#5#p3xmd35r_$*'

ENVIRONMENT = config("ENVIRONMENT", default="development")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool, default=False)

#ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.0.107', config('SERVER', default='127.0.0.1')]
ALLOWED_HOSTS = [host for host in config("ALLOWED_HOSTS").split(",")]

#URLS API
BINACE_API_URL = config("BINANCE_API_URL")
CONTRADECX_API_URL = config("CONTRADECX_API_URL")
BITCAMBIO_API_URL = config("BITCAMBIO_API_URL")
BRASIL_BITCOIN_API_URL = config("BRASIL_BITCOIN_API_URL")
BITCOIN_TRADE_API_URL = config("BITCOIN_TRADE_API_URL")
FOXBIT_API_URL = config("FOXBIT_API_URL")
NOVADAX_API_URL = config("NOVADAX_API_URL")
MERCADO_BITCOIN_API_URL = config("MERCADO_BITCOIN_API_URL")
BITPRECO_API_URL = config("BITPRECO_API_URL")
BITCOIN_TO_YOU_API_URL = config("BITCOIN_TO_YOU_API_URL")

#KEYS API
BINANCE_API_KEY = config("BINANCE_API_KEY")
CONTRADECX_API_KEY = config("CONTRADECX_API_KEY")
BITCAMBIO_API_KEY = config("BITCAMBIO_API_KEY")
BRASIL_BITCOIN_API_KEY = config("BRASIL_BITCOIN_API_KEY")
BITCOIN_TRADE_API_KEY = config("BITCOIN_TRADE_API_KEY")
FOXBIT_API_KEY = config("FOXBIT_API_KEY")
NOVADAX_API_KEY = config("NOVADAX_API_KEY")
MERCADO_BITCOIN_API_KEY = config("MERCADO_BITCOIN_API_KEY")
BITPRECO_API_KEY = config("BITPRECO_API_KEY")
BITCOIN_TO_YOU_API_KEY = config("BITCOIN_TO_YOU_API_KEY")



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'rest_framework',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'denarios.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'denarios.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_heroku.settings(locals())
