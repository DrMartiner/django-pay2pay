# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from views import Paypage

urlpatterns = patterns('',
    url(r'^pay2pay/', include('pay2pay.urls')),
    url(r'^pay-page/$', Paypage.as_view(), name='pay_page'),
)
