__author__ = 'nadiya'
from django.conf.urls import patterns, url,include
from views import LoginView,

urlpatterns = patterns('',
    url(r'^login$',LoginView.as_view(),name='index'),
    )