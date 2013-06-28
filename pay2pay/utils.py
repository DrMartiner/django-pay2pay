# -*- coding: utf-8 -*-

import base64
import hashlib
import lxml.etree
import lxml.builder


def build_xml_string(data):
    e = lxml.builder.ElementMaker()

    request = e.request
    version = e.version
    merchant_id = e.merchant_id
    order_id = e.order_id
    amount = e.amount
    currency = e.currency
    description = e.description
    success_url = e.success_url
    fail_url = e.fail_url
    result_url = e.result_url
    test_mode = e.test_mode

    request = request(
        version(data['version']),
        merchant_id(str(data['merchant_id'])),
        order_id(data['order_id']),
        amount(str(data['amount'])),
        currency(data['currency']),
        description(data['description']),
        success_url(data['success_url']),
        fail_url(data['fail_url']),
        result_url(data['result_url']),
        test_mode(
            str(data.get('test_mode', ''))
        ),
    )
    return lxml.etree.tostring(request, encoding='utf-8').replace('\n', '')


def get_signature(xml, key):
    sign_str = '{0}{1}{0}'.format(key, xml)
    hsh = hashlib.md5()
    hsh.update(sign_str)
    sign_md5 = hsh.hexdigest()
    sign_encode = base64.b64encode(sign_md5)
    return sign_encode