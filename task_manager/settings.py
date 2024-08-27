"""
Django settings for task_manager project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import logging
import os
import uuid

import dj_database_url
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

logger = logging.getLogger(__name__)

# env variables
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY") or uuid.uuid4()

USE_LOCAL_DB = os.getenv("USE_LOCAL_DB") == 'true'
DATABASE_URL = os.getenv("DATABASE_URL")

# Set DEBUG if DJ_DEBUG at environment vars is true
DEBUG = os.getenv('DJ_DEBUG') == 'true'
if DEBUG:
    logger.info("You started in debug mode")

ALLOWED_HOSTS = [
    'webserver',
]

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bootstrap5',
    'django_extensions',
    'crispy_forms',
    'crispy_bootstrap5',
    'task_manager',
    'users',
    'statuses',
    'tasks',
    'labels',
]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

ROOT_URLCONF = 'task_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'task_manager.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if USE_LOCAL_DB:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'mydb.sqlite3',
            'TEST': {
                'NAME': BASE_DIR / 'mytestdatabase',
            },
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 3,
        }
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ("ru", _("Russian")),
    ("en", _("English")),
)

LOCALE_PATHS = [BASE_DIR / "locale"]

LOGIN_URL = '/login/'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if not DEBUG:
    ROLLBAR = {
        'access_token': os.getenv("ROLLBAR_TOKEN"),
        'environment': 'development' if DEBUG else 'production',
        'code_version': '1.0',
        'root': BASE_DIR,
    }
