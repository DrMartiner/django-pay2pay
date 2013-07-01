=====
Dajngo pay2pay
=====

Приложения для приема платежей через систему http://pay2pay.com

=====
Quick start
=====

1. Добавляем 'pay2pay' INSTALLED_APPS::

      INSTALLED_APPS = (
            ...
            'pay2pay',
      )

2. Добавить ``url(r'^pay2pay/', include('pay2pay.urls')),`` в urls.py

3. Обязательные параметры settings.py::

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

4. Выполните ``python manage.py syncdb`` для создание таблицы с заказазами или выполните мограцию, если вы используете south: ``python manage.py migrate pay2pay2``


5. Определите три шаблона::

      pay2pay/payment_fail.html # Для отменных платежей
      pay2pay/payment_success.html # Для успешных платежей

