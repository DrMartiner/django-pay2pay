# -*- coding: utf-8 -*-

import factory
from .models import Order


class OrderF(factory.Factory):
    FACTORY_FOR = Order