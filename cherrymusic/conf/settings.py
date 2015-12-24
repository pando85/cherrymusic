"""
Django settings for cherrymusic project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."),)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'ext'))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ywps9g4&cs-fs)118(4snx8cb&185wr=d)7b+2hh#vw5*o!f5@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'core.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'pipeline',
    'core',
    'storage',
    'client',
    'djangobower',
    'rest_auth'
]

OLD_PASSWORD_FIELD_ENABLED = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'conf.urls'

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

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'conf/db.sqlite3'),
        }
}

# bower config
BOWER_INSTALLED_APPS = (
    'angular',
    'bootstrap',
    'angular-bootstrap',
    'angular-resource',
    'jquery',
    'jplayer',
    'dndLists',
    'underscore',
    'angular-dropdowns',
    'angular-cookies',
    'json3',
    'es5-shim',
    'angular-sanitize',
    'angular-route',
    'chieffancypants/angular-hotkeys',
)

# pipeline config
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
    'djangobower.finders.BowerFinder',
)
PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'

PIPELINE_CSS = {
    'client': {
        'source_filenames': (
            'client/bower_components/bootstrap/dist/css/bootstrap.css',
            'client/style/cherrymusic.less',
            'client/style/filebrowser.less',
            'client/style/mediaplayer.less',
            'client/style/playlist.less',
            'client/style/variables.less',
            'client/style/dropdowns.less',
        ),
        'output_filename': 'client/cherrymusic.css',
        }
}
PIPELINE_JS = {
    'client': {
        'source_filenames': (
            'client/bower_components/angular/angular.js',
            'client/bower_components/angular-resource/angular-resource.js',
            'client/bower_components/angular-drag-and-drop-lists/angular-drag-and-drop-lists.js',
            'client/bower_components/angular-bootstrap/ui-bootstrap.js',
            'client/bower_components/angular-bootstrap/ui-bootstrap-tpls.js',
            'client/bower_components/jquery/dist/jquery.js',
            'client/bower_components/jPlayer/dist/jplayer/jquery.jplayer.js',
            'client/bower_components/underscore/underscore.js',
            'client/bower_components/angular-dropdowns/dist/angular-dropdowns.js',
            'client/bower_components/angular-cookies/angular-cookies.js',
            'client/bower_components/json3/lib/json3.js',
            'client/bower_components/es5-shim/es5-shim.js',
            'client/bower_components/angular-sanitize/angular-sanitize.js',
            'client/bower_components/angular-route/angular-route.js',
            'client/bower_components/angular-hotkeys/build/hotkeys.js',
            'client/js/main.js',
            'client/js/auth-user/django_auth.js',
            'client/js/auth-user/validate.js',
            'client/js/controllers/change_password.js',
            'client/js/controllers/dropdown_top_menu.js',
            'client/js/controllers/main_view.js',
            'client/js/controllers/jplayer.js',
            'client/js/controllers/playlists.js',
            'client/js/directives/progressbar.js',
            'client/js/directives/file.js',
            'client/js/directives/filebrowser.js',
            'client/js/directives/playlist.js',
            'client/js/directives/playlistbrowser.js',
            'client/js/filters/timeformat.js',
            'client/js/resources/browse.js',
            'client/js/resources/index_directory.js',
            'client/js/resources/playlist.js',
            'client/js/resources/track.js',
            'client/js/resources/user.js',
            'client/js/hotkeys.js',
            'client/js/mediaplayer.js',
            'client/js/playback_service.js',
            'client/js/playback_service_jplayer.js',
        ),
        'output_filename': 'client/cherrymusic.js'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'client', 'static', 'client')
