# coding: utf-8

from django.conf.urls import url

from diary import views

urlpatterns = [
    url(r'^$', views.homepage,
        name="homepage"),
]