from django.contrib import admin
from blog.models import BlogPost, HeaderElement, ArcheryClassType, ArcheryClass
from django import forms

admin.site.register(BlogPost)
admin.site.register(HeaderElement)
admin.site.register(ArcheryClassType)
admin.site.register(ArcheryClass)
