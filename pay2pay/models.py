# -*- coding: utf-8 -*-

import conf
import uuid
from django.db import models
from .utils import build_xml_string
from .utils import get_signature


class Order(models.Model):
    version = models.CharField('Версия интерфейса', max_length=8, default='1.3')
    merchant_id = models.PositiveIntegerField('ID магазина', default=conf.PAY2PAY_MERCHANT_ID)
    order_id = models.CharField('Номер заказа', max_length=32, default=lambda: str(uuid.uuid4()))
    amount = models.FloatField('Сумма', default=.0)
    currency = models.CharField('Валюта', max_length=8, default=conf.PAY2PAY_CURRENCY)
    description = models.CharField('Описание', max_length=512, default='')

    paymode = models.CharField('Способ платежа', max_length=16, blank=True, null=True)
    trans_id = models.CharField('Номер транзакции', max_length=32, blank=True, null=True)
    status = models.CharField('Статус', max_length=16, blank=True, null=True)
    error_msg = models.CharField('Описание ошибки', max_length=256, blank=True, null=True)

    created = models.DateTimeField('Создан', auto_now_add=True)

    @property
    def signature(self):
        return get_signature(self.xml, conf.PAY2PAY_SEKRET_KEY)

    @property
    def xml(self):
        data = self._get_xml_data()
        return build_xml_string(data)

    def _get_xml_data(self):
        names = []
        for field in self._meta.fields:
            if field.name == 'created':
                continue
            names.append(field.name)

        data = {
            'success_url': conf.PAY2PAY_SUCCESS_URL,
            'fail_url': conf.PAY2PAY_FAIL_URL,
            'result_url': conf.PAY2PAY_RESULT_URL,
        }
        for name in names:
            value = getattr(self, name)
            if value:
                data[name] = value

        return data

    class Meta:
        ordering = ('created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'