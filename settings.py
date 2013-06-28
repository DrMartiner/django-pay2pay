import sys
import os.path

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ''))
sys.path.insert(0, ROOT)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

PAY2PAY_MERCHANT_ID = 2669
PAY2PAY_SEKRET_KEY = 'qCmm7SNTSdasfsqCmm7SNTSd'
PAY2PAY_FAIL_URL = 'http://127.0.0.1:8000/fail/'
PAY2PAY_SUCCESS_URL = 'http://127.0.0.1:8000/success/'
PAY2PAY_RESULT_URL = 'http://127.0.0.1:8000/success/'
PAY2PAY_TEST_MODE = True

SECRET_KEY = '!!!very_secret!!!'
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'factory',
    'pay2pay',
)

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










