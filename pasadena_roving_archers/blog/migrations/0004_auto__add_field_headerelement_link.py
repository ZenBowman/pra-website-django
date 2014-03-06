# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'HeaderElement.link'
        db.add_column(u'blog_headerelement', 'link',
                      self.gf('django.db.models.fields.TextField')(default='foo.html', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'HeaderElement.link'
        db.delete_column(u'blog_headerelement', 'link')


    models = {
        u'blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'blog.enrichedblogpost': {
            'Meta': {'object_name': 'EnrichedBlogPost'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'short_text': ('redactor.fields.RedactorField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'blog.headerelement': {
            'Meta': {'object_name': 'HeaderElement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['blog']