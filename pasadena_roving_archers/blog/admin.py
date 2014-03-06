from django.contrib import admin
from blog.models import BlogPost, HeaderElement
from django import forms
from redactor.widgets import RedactorEditor

admin.site.register(BlogPost)
admin.site.register(HeaderElement)
