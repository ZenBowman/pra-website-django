from django.contrib import admin
from blog.models import BlogPost, HeaderElement, ArcheryClassType, ArcheryClass, ClassRegistration
from django import forms

admin.site.register(BlogPost)
admin.site.register(HeaderElement)
admin.site.register(ArcheryClassType)
admin.site.register(ArcheryClass)
admin.site.register(ClassRegistration)

