"""
Django settings for myblogapp project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0e-8-1aqndxx22i#v+!(n=vdn!6xk_^c2pn0h*)ec$4x8fkow3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['127.0.0.1', '52.69.7.213','.carekyo.com.','carekyo.com',]

# Application definition

INSTALLED_APPS = [
    'posts.apps.PostsConfig',
    'community.apps.CommunityConfig',
    'accounts.apps.AccountsConfig',
    'tags.apps.TagsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myblogapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'myblogapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE':'django.db.backends.postgresql_psycopg2',
        # 'NAME':'myblogapp',
        # 'USER':'mybloguser',
        # 'PASSWORD':'Passw0rd1',
        # 'HOST':'myblogapp.c6u0bhzbqqfv.ap-northeast-1.rds.amazonaws.com',
        # 'PORT':'',

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myblogapp',
        'USER': 'myblogapp',
        'PASSWORD': 'dragonta',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
#MEDIA_URL = '/pics/media/'
MEDIA_URL = '/pics/'
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
#MEDIA_ROOT = os.path.join(BASE_DIR. '/posts/pics')
#MEDIA_ROOT = BASE_DIR
MEDIA_ROOT = os.path.join(BASE_DIR, 'pics')

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/community/'
LOGOUT_REDIRECT_URL = '/community/'

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

