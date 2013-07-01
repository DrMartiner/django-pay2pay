# -*- coding: utf-8 -*-

import conf
import uuid
from django.db import models
from .signals import payment_process
from .signals import payment_completed
from .signals import payment_fail
from .utils import build_xml_string
from .utils import get_signature


class Payment(models.Model):
    STATUS_NOT_SEND = 'not_send'
    STATUS_PROCESS = 'process'
    STATUS_RESERVE = 'reserve'
    STATUS_SUCCESS = 'success'
    STATUS_FAIL = 'fail'
    STATUS_CHOICES = (
        (STATUS_NOT_SEND, 'Не отправлен'),
        (STATUS_PROCESS, 'Ожидается оплата'),
        (STATUS_RESERVE, 'Средства зарезервированы'),
        (STATUS_SUCCESS, 'заказ оплачен'),
        (STATUS_FAIL, 'Оплата отменена'),
    )
    version = models.CharField('Версия интерфейса', max_length=8, default='1.3')
    merchant_id = models.PositiveIntegerField('ID магазина', default=conf.PAY2PAY_MERCHANT_ID)
    order_id = models.CharField('Номер заказа', max_length=16, default=lambda: str(uuid.uuid4()).replace('-', '')[:16])
    amount = models.FloatField('Сумма', default=.0)
    currency = models.CharField('Валюта', max_length=8, default=conf.PAY2PAY_CURRENCY)
    description = models.CharField('Описание', max_length=512, default='')

    paymode = models.CharField('Способ платежа', max_length=16, blank=True, null=True)
    trans_id = models.CharField('Номер транзакции', max_length=32, blank=True, null=True)
    status = models.CharField('Статус', max_length=16, choices=STATUS_CHOICES, default=STATUS_NOT_SEND)
    error_msg = models.CharField('Описание ошибки', max_length=256, blank=True, null=True)
    test_mode = models.BooleanField('Тестовый режим', default=conf.PAY2PAY_TEST_MODE)

    updated = models.DateTimeField('Обновлен', auto_now=True)
    created = models.DateTimeField('Создан', auto_now_add=True)

    def __unicode__(self):
        return '%s <%s>' % (
            self.order_id,
            self.get_status_display()
        )

    def send_signals(self):
        if not self.status:
            return

        status = self.status
        if status == self.STATUS_PROCESS or status == self.STATUS_RESERVE:
            payment_process.send(sender=self)
        if status == self.STATUS_SUCCESS:
            payment_completed.send(sender=self)
        if status == self.STATUS_FAIL:
            payment_fail.send(sender=self)

    @property
    def signature(self):
        return get_signature(self.xml, conf.PAY2PAY_SECRET_KEY)

    @property
    def xml(self):
        data = self._get_xml_data()
        return build_xml_string(data)

    def _get_xml_data(self):
        data = {
            'success_url': conf.PAY2PAY_SUCCESS_URL,
            'fail_url': conf.PAY2PAY_FAIL_URL,
            'result_url': conf.PAY2PAY_RESULT_URL,
        }
        if conf.PAY2PAY_TEST_MODE:
            data['test_mode'] = 1
        for name in self.names:
            value = getattr(self, name)
            if value:
                data[name] = value

        return data

    names = [
        'version',
        'merchant_id',
        'order_id',
        'amount',
        'currency',
        'description',
    ]

    class Meta:
        ordering = ('created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'