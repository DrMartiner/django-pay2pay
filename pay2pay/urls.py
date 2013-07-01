# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import Confirm
from .views import PaymentFail
from .views import PaymentSuccess

urlpatterns = patterns('',
    url(r'^confirm/$', Confirm.as_view(), name='pay2pay_confirm'),
    url(r'^success/$', PaymentFail.as_view(), name='pay2pay_success'),
    url(r'^fail/$', PaymentSuccess.as_view(), name='pay2pay_fail'),
)