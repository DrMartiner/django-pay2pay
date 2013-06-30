# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'amount', 'currency', 'paymode', 'status', 'trans_id', 'description', 'created')
    list_filter = ('merchant_id', 'paymode', 'status', 'created')
    search_fields = ('order_id', 'description', 'error_msg')

    can_delete = False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Payment, PaymentAdmin)