from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns(
    '',
    url(r'^register/thanks', views.thanks, name='thanks'),
    url(r'^register', views.register, name='register'),
    url(r'^$', views.index, name='index')
)
