# -*- coding: utf-8 -*-

import base64
from mock import patch
from django.conf import settings
from django.test import TestCase
from django_webtest import WebTest
from django.core.urlresolvers import reverse
from django.test.utils import override_settings
from .utils import build_xml_string
from .utils import get_signature
from .factories import OrderF
from .models import Order


class UtilsTest(TestCase):
    def setUp(self):
        self.xml = '<request><version>1.3</version><merchant_id>2669</merchant_id><order_id>0143ef7d</order_id><amount>1.0</amount><currency>RUB</currency><description>Описание заказа</description><success_url>http://localhost:8000/success/</success_url><fail_url>http://localhost:8000/fail/</fail_url><result_url>http://localhost:8000/success/</result_url><test_mode>1</test_mode></request>'

    def test_build_xml_string(self):
        data = {
            'test_mode': 1,
            'version': u'1.3',
            'order_id': '0143ef7d',
            'fail_url': 'http://localhost:8000/fail/',
            'currency': u'RUB',
            'amount': 1.0,
            'result_url': 'http://localhost:8000/success/',
            'success_url': 'http://localhost:8000/success/',
            'merchant_id': 2669,
            'description': u'\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430'
        }
        xml = build_xml_string(data)

        self.assertEquals(self.xml, xml, 'XML built is wrong')

    @override_settings(PAY2PAY_SECRET_KEY='qCmm7dsaSdasfsqCmgdjfgkdfghdfsad')
    def test_get_signature(self):
        sign_encode = get_signature(self.xml, settings.PAY2PAY_SECRET_KEY)
        self.assertEquals('MzVlMDJiZmFlODU4ZDM2MWNiZDJkZGM0ZmRkMzQ0OWY=', sign_encode, 'XML not signed')


class OrderModelTest(TestCase):
    @patch('uuid.uuid4', lambda: 'ea2fe31e')
    def test_get_xml_data(self):
        test_data = {
            'version': u'1.3',
            'order_id': 'ea2fe31e',
            'fail_url': 'http://localhost:8000/fail/',
            'currency': u'RUB',
            'result_url': 'http://localhost:8000/success/',
            'success_url': 'http://localhost:8000/success/',
            'merchant_id': 2669,
        }

        order = Order()
        data = order._get_xml_data()

        self.assertEquals(test_data, data, 'Data from Order model was wrong')


class ConfirmTest(WebTest):
    def setUp(self):
        self.xml = """<?xml version="1.0" encoding="UTF-8"?>
            <response>
                <version>1.3</version>
                <merchant_id>10</merchant_id>
                <type>result</type>
                <language>ru</language>
                <order_id>O_123</order_id>
                <amount>10.50</amount>
                <currency>RUB</currency>
                <description>Описание</description>
                <paymode>Paymode_Code</paymode>
                <trans_id>12345</trans_id>
                <status>success</status>
                <error_msg></error_msg>
                <test_mode>1</test_mode>
                <other>data</other>
                <paydata>...</paydata>
            </response>
        """

        order = OrderF(order_id='O_123')
        order.save()

    def _get_obj_response(self, xml):
        return {
            'status': 'success',
            'test_mode': '1',
            'description': u'Описание',
            'order_id': 'O_123',
            'error_msg': '',
            'paymode': 'Paymode_Code',
            'currency': 'RUB',
            'amount': 10.50,
            'version': '1.3',
            'merchant_id': 2669,
            'trans_id': '12345'
        }

    def _get_signature(self, key):
        return 'YzU3N2Y4MTNlNzUyNTRkODhiZWFiOWIwNjFlOWNiOTQ='

    @override_settings(PAY2PAY_HIDE_KEY='qCmm7SNTSdasfsqCmm7SNTSd')
    @patch('pay2pay.views.Confirm._get_obj_response', _get_obj_response)
    @patch('pay2pay.utils.get_signature', _get_signature)
    def test_update_status(self):
        xml_encode = base64.b64encode(self.xml)
        sign_encode = get_signature(self.xml, settings.PAY2PAY_HIDE_KEY)

        params = {
            'xml': xml_encode,
            'sign': sign_encode,
        }
        url = reverse('pay2pay_confirm')
        self.app.post(url, params=params)

        order = Order.objects.get(order_id='O_123')
        self.assertEquals(order.status, 'success', 'Order status was not updated')

    @override_settings(PAY2PAY_HIDE_KEY='qCmm7SNTSdasfsqCmm7SNTSd')
    def test_confirm_response(self):
        xml_encode = base64.b64encode(self.xml)
        sign_encode = get_signature(self.xml, settings.PAY2PAY_HIDE_KEY)

        params = {
            'xml': xml_encode,
            'sign': sign_encode,
        }
        url = reverse('pay2pay_confirm')
        response = self.app.post(url, params=params)

        self.assertEquals(200, response.status_code, 'Confirm view is unavalible')
        self.assertIn('<status>yes</status>', response.text, 'Response has not status yes')
        self.assertIn('<error_msg></error_msg>', response.text, 'Response have error message')
