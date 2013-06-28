# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.generic import View


class Confirm(View):
    def post(self, request, *args, **kwargs):
        return HttpResponse()