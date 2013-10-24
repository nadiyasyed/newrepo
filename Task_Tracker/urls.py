from django.conf.urls import patterns, include, url
from django.conf import settings
from accounts import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',


        url(r'^$',views.SignupView.as_view()),


    )
