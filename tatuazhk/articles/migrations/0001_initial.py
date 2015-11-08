# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'articles_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('short_description', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('content', self.gf('ckeditor.fields.RichTextField')()),
        ))
        db.send_create_signal(u'articles', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'articles_post')


    models = {
        u'articles.post': {
            'Meta': {'object_name': 'Post'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'short_description': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['articles']