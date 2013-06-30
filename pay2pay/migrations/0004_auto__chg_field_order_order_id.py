# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Payment.order_id'
        db.alter_column(u'pay2pay_payment', 'order_id', self.gf('django.db.models.fields.CharField')(max_length=16))

    def backwards(self, orm):

        # Changing field 'Payment.order_id'
        db.alter_column(u'pay2pay_payment', 'order_id', self.gf('django.db.models.fields.CharField')(max_length=32))

    models = {
        u'pay2pay.order': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Payment'},
            'amount': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'RUB'", 'max_length': '8'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512'}),
            'error_msg': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2669'}),
            'order_id': ('django.db.models.fields.CharField', [], {'default': "'180524c9-932d-45'", 'max_length': '16'}),
            'paymode': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'test_mode': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'trans_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.3'", 'max_length': '8'})
        }
    }

    complete_apps = ['pay2pay']