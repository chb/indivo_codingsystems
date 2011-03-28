# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CodingSystem'
        db.create_table('codingsystems_codingsystem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True)),
            ('key_field_name_1', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('key_field_name_2', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('key_field_name_3', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('key_field_name_4', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
        ))
        db.send_create_signal('codingsystems', ['CodingSystem'])

        # Adding model 'CodedValue'
        db.create_table('codingsystems_codedvalue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['codingsystems.CodingSystem'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('physician_value', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('consumer_value', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('umls_code', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('key_field_value_1', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('key_field_value_2', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('key_field_value_3', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('key_field_value_4', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('additional_fields', self.gf('codingsystems.models.JSONField')(null=True)),
        ))
        db.send_create_signal('codingsystems', ['CodedValue'])

        # Adding unique constraint on 'CodedValue', fields ['system', 'code']
        db.create_unique('codingsystems_codedvalue', ['system_id', 'code'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'CodedValue', fields ['system', 'code']
        db.delete_unique('codingsystems_codedvalue', ['system_id', 'code'])

        # Deleting model 'CodingSystem'
        db.delete_table('codingsystems_codingsystem')

        # Deleting model 'CodedValue'
        db.delete_table('codingsystems_codedvalue')


    models = {
        'codingsystems.codedvalue': {
            'Meta': {'unique_together': "(('system', 'code'),)", 'object_name': 'CodedValue'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'additional_fields': ('codingsystems.models.JSONField', [], {'null': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'consumer_value': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_field_value_1': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'key_field_value_2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'key_field_value_3': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'key_field_value_4': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'physician_value': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['codingsystems.CodingSystem']"}),
            'umls_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'})
        },
        'codingsystems.codingsystem': {
            'Meta': {'object_name': 'CodingSystem'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_field_name_1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'key_field_name_2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'key_field_name_3': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'key_field_name_4': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['codingsystems']
