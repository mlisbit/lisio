import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MEDIA_ROOT = BASE_DIR+'/static'
print MEDIA_ROOT
MEDIA_URL = ''

secrets = json.load(file(BASE_DIR+'/../secrets.json'))
SECRET_KEY = secrets['SECRET_KEY']

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lisio',
    'projects',
    'home',
    'resume',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lisio.urls'

WSGI_APPLICATION = 'lisio.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': secrets['DB_ENGINE'], 
        'NAME': secrets['DB_NAME'],
        'USER': secrets['DB_USER'],
        'PASSWORD': secrets['DB_PASSWORD'],
        'HOST': secrets['DB_HOST'],                      
        'PORT': secrets['DB_PORT'],                      
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    BASE_DIR+'/lisio/templates',
    BASE_DIR+'/projects/templates',
)

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    BASE_DIR+'/static',
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)



