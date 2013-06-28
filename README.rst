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

      WMI_MERCHANT_ID = '1234567890123' # Номер кошелька продавца
      WMI_MERCHANT_SEKRET_KEY = 'secret key!' # Задается в ["Личном кабинете"](https://www.walletone.com/client/)
      WMI_CURRENCY_ID_DEFAULT = 643 # ID валюты (по умолчанию рубли)
      WMI_SUCCESS_URL = 'http://example.com/success/' #
      WMI_FAIL_URL = 'http://example.com/success/' #
      WMI_EXPIRED_DAYS = 3 # Дата истечения заказа (по умолчанию 3)
      WMI_PTENABLED = [] # Список из строк с разрешенными способами оплаты
      WMI_PTDISABLED = [] # Список из строк с запрещенными способами оплаты
      WMI_CULTURE_ID = 'ru-RU' # По умолчанию русский, также может быть 'en-EN'

4. Выполните ``python manage.py syncdb`` для создание таблицы с заказазами.


=====
Usage
=====

Генерация формы оплаты

views.py::

      # -*- coding: utf-8 -*-

      from django.views.generic import TemplateView
      from w1.forms import PayForm


      class Paypage(TemplateView):
          template_name = 'pay_page.html'

          def get_context_data(self, **kwargs):
              ctx = super(Paypage, self).get_context_data(**kwargs)
              ctx['form'] = PayForm(initial={
                  'WMI_PAYMENT_AMOUNT': 11.22,
                  'WMI_DESCRIPTION': u'описание заказа',
              })
              return ctx

pay_page.html::

      <form method="post" action="https://merchant.w1.ru/checkout/default.aspx" accept-charset="UTF-8">
          <ul style="list-style: none;">
              {{ form.as_ul|safe }}
              <li>
                  <input type="submit" />
              </li>
          </ul>
      </form>

