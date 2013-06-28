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

4. Выполните ``python manage.py syncdb`` для создание таблицы с заказазами.


=====
Usage
=====