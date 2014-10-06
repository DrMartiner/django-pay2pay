# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from pay2pay.forms import PayForm


class Paypage(TemplateView):
    template_name = 'pay2pay/pay_page.html'

    def get_context_data(self, **kwargs):
        ctx = super(Paypage, self).get_context_data(**kwargs)
        ctx['form'] = PayForm(initial={
            'amount': 1.0,
            'description': u'Описание заказа',
        })
        return ctx