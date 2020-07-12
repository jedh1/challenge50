"""
Django settings for challenge project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
import dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load local environment vars when running localy
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    # local settings
    dotenv.load_dotenv(dotenv_file)
    DATABASES = {
        'default': {
            'ENGINE': os.getenv("db_engine"),
            'NAME': os.getenv("db_name"),
            'USER': os.getenv("db_user"),
            'PASSWORD': os.getenv("db_password"),
            'HOST': os.getenv("db_host"),
            'PORT': os.getenv("db_port"),
        }
    }
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = os.getenv("DEBUG")

    # Email settings local
    EMAIL_HOST = os.getenv("EMAIL_HOST")
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
    EMAIL_PORT = os.getenv("EMAIL_PORT")
    EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
    SERVER_EMAIL = EMAIL_HOST_USER
else:
    # Production settings
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = os.environ.get('debug_heroku')
    # https://docs.djangoproject.com/en/3.0/ref/settings/#databases
    import dj_database_url
    DATABASES = {'default': dj_database_url.config(conn_max_age=600)}
    # Email settings heroku
    EMAIL_USE_TLS = True
    EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER', '')
    EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT', '')
    EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN', '')
    EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD', '')
    SERVER_EMAIL = 'csprojects200220@gmail.com'

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_apscheduler',
    'background_task',
    'projects',
    'blog',
    'hotelm',
    'backtest',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'challenge.urls'

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

WSGI_APPLICATION = 'challenge.wsgi.application'

# Database

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)--------------------------
# https://docs.djangoproject.com/en/3.0/howto/static-files/-------

# URL for static files: www.test.com/static/test.jpg
STATIC_URL = '/static/'
# location where django collects all static files
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#
# Determines where static files are pulled from. Extra places for collectstatic to find static files for Heroku
STATICFILES_DIRS = [os.path.join(BASE_DIR,'projects/static/')]

# background task settings
MAX_ATTEMPTS = 1
BACKGROUND_TASK_RUN_ASYNC = True

# apscheduler settings
# This scheduler config will:
# - Store jobs in the project database
# - Execute jobs in threads inside the application process
SCHEDULER_CONFIG = {
    "apscheduler.jobstores.default": {
        "class": "django_apscheduler.jobstores:DjangoJobStore"
    },
    'apscheduler.executors.processpool': {
        "type": "threadpool"
    },
}
SCHEDULER_AUTOSTART = True
APSCHEDULER_DATETIME_FORMAT =  "N j, Y, f:s a"  # Default

ADMINS = [('jed', 'jedhcl@gmail.com')]

if not os.path.isfile(dotenv_file):
    django_heroku.settings(locals())
    del DATABASES['default']['OPTIONS']['sslmode']
