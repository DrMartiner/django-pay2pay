# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Payment'
        db.create_table(u'pay2pay_payment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version', self.gf('django.db.models.fields.CharField')(default='1.3', max_length=8)),
            ('merchant_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=2669)),
            ('order_id', self.gf('django.db.models.fields.CharField')(default='a4f3990ab2ae4c96', max_length=16)),
            ('amount', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('currency', self.gf('django.db.models.fields.CharField')(default='RUB', max_length=8)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=512)),
            ('paymode', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('trans_id', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='not_send', max_length=16)),
            ('error_msg', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('test_mode', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'pay2pay', ['Payment'])


    def backwards(self, orm):
        # Deleting model 'Payment'
        db.delete_table(u'pay2pay_payment')


    models = {
        u'pay2pay.payment': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Payment'},
            'amount': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'RUB'", 'max_length': '8'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512'}),
            'error_msg': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2669'}),
            'order_id': ('django.db.models.fields.CharField', [], {'default': "'3be556531c604af2'", 'max_length': '16'}),
            'paymode': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'not_send'", 'max_length': '16'}),
            'test_mode': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'trans_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.3'", 'max_length': '8'})
        }
    }

    complete_apps = ['pay2pay']