from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^register.html', views.register, name='register'),
    url(r'^$', views.index, name='index')
)
