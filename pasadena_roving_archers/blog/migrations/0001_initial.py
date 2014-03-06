# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EnrichedBlogPost'
        db.create_table(u'blog_enrichedblogpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('short_text', self.gf('redactor.fields.RedactorField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'blog', ['EnrichedBlogPost'])

        # Adding model 'BlogPost'
        db.create_table(u'blog_blogpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('image', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'blog', ['BlogPost'])


    def backwards(self, orm):
        # Deleting model 'EnrichedBlogPost'
        db.delete_table(u'blog_enrichedblogpost')

        # Deleting model 'BlogPost'
        db.delete_table(u'blog_blogpost')


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
        }
    }

    complete_apps = ['blog']