# coding: utf-8

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from diary import views

urlpatterns = [
    url(r'^$', views.api_root,
        name="root"),

    url(r'^entry/list/$', views.EntryList.as_view(),
        name="entry_list"),
    url(r'^entry/(?P<pk>[0-9]+)/$', views.EntryDetail.as_view(),
        name="entry_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)