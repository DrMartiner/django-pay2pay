=====
Dajngo pay2pay
=====

Приложения для приема платежей через систему http://pay2pay.com

=====
Quick start
=====

0. Устанавливаем приложение::

      pip install django-pay2pay

1. Добавляем 'pay2pay' INSTALLED_APPS::

      INSTALLED_APPS = (
            ...
            'pay2pay',
      )

2. Добавить ``url(r'^pay2pay/', include('pay2pay.urls')),`` в urls.py

3. Обязательные параметры settings.py (находятся в https://cp.pay2pay.com/ ) ::

      PAY2PAY_MERCHANT_ID = 1111
      PAY2PAY_HIDE_KEY = 'qCmm7SNTSdasfsqCmm7SNTSd'
      PAY2PAY_SECRET_KEY = 'qCmm7dsaSdasfsqCmgdjfgkdfghdfsad'
      PAY2PAY_FAIL_URL = 'http://example.com/pay2pay/fail/'
      PAY2PAY_SUCCESS_URL = 'http://example.com/pay2pay/success/'
      PAY2PAY_RESULT_URL = 'http://example.com/pay2pay/confirm/'

4. Добавить логер с именем ``pay2pay``::

      LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
        'standart': {
            'format': '(%(asctime)s) %(levelname)s [%(filename)s -> %(funcName)s -> %(lineno)d]: "%(message)s"',
        }
          },
          'handlers': {
              'pay2pay': {
                  'level': 'DEBUG',
                  'class': 'logging.handlers.WatchedFileHandler',
                  'filename': os.path.join(ROOT, 'pay2pay.log'),
                  'formatter': 'standart'
              }
          },
          'loggers': {
              'pay2pay': {
                  'handlers': ['pay2pay'],
                  'level': 'DEBUG',
                  'propagate': True
              }
          }
      }

4. Выполните ``python manage.py syncdb`` для создание таблицы с заказазами или выполните мограцию, если вы используете south: ``python manage.py migrate pay2pay2``


5. Определите два шаблона::

      pay2pay/payment_fail.html # Для отменных платежей
      pay2pay/payment_success.html # Для успешных платежей

