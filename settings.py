# -*- coding: utf-8 -*-

import sys
import os.path

try:
    from settings_local import *
except ImportError:
    print "Don't forget create settings_local.py"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ''))
sys.path.insert(0, ROOT)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

STATIC_URL = '/static/'

PAY2PAY_MERCHANT_ID = 1111
PAY2PAY_HIDE_KEY = 'qCmm7SNTSdasfsqCmm7SNTSd'
PAY2PAY_SEKRET_KEY = 'qCmm7dsaSdasfsqCmgdjfgkdfghdfsad'
PAY2PAY_FAIL_URL = 'http://localhost:8000/fail/'
PAY2PAY_SUCCESS_URL = 'http://localhost:8000/success/'
PAY2PAY_RESULT_URL = 'http://localhost:8000/success/'
PAY2PAY_TEST_MODE = True

SECRET_KEY = '!!!very_secret!!!'
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'south',
    'factory',
    'pay2pay',
)

SOUTH_TESTS_MIGRATE = False
SKIP_SOUTH_TESTS = True

INTERNAL_IPS = [
    'localhost',
    '127.0.0.1',
]

TEMPLATE_DIRS = (
    os.path.join(ROOT, 'templates'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        }
    },
    'handlers': {
        'pay2pay': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(ROOT, 'pay2pay.log'),
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'pay2pay': {
            'handlers': ['pay2pay'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}

try:
    from settings_local import *
except ImportError:
    pass