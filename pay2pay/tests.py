# -*- coding: utf-8 -*-

from mock import patch
from django.conf import settings
from django.test import TestCase
from django_webtest import WebTest
from django.test.utils import override_settings
from .utils import get_signature
from .utils import build_xml_string
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

    @override_settings(PAY2PAY_SEKRET_KEY='qCmm7dsaSdasfsqCmgdjfgkdfghdfsad')
    def test_get_signature(self):
        sign_encode = get_signature(self.xml, settings.PAY2PAY_SEKRET_KEY)
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
    def test_confirm(self):
        pass