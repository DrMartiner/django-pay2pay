# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import Confirm

urlpatterns = patterns('',
    url(r'^confirm/$', Confirm.as_view(), name='pay2pay_confirm'),
)