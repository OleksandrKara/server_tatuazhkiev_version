# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Foto'
        db.create_table(u'fotos_foto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('comment_first', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('comment_second', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('type', self.gf('django.db.models.fields.CharField')(default='Br', max_length=2)),
            ('image_location', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'fotos', ['Foto'])


    def backwards(self, orm):
        # Deleting model 'Foto'
        db.delete_table(u'fotos_foto')


    models = {
        u'fotos.foto': {
            'Meta': {'object_name': 'Foto'},
            'comment_first': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'comment_second': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_location': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Br'", 'max_length': '2'})
        }
    }

    complete_apps = ['fotos']