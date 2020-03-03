# coding: utf-8

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    url(r"^$", views.api_root, name="api_root"),
    url(r"^entry/list/$", views.EntryList.as_view(), name="entry_list"),
    url(r"^entry/(?P<pk>[0-9]+)/$", views.EntryDetail.as_view(), name="entry_detail"),
    url(r"^status/list/$", views.StatusEntryList.as_view(), name="status_list"),
    url(
        r"^status/change/(?P<entry_pk>[0-9]+)/$",
        views.change_status,
        name="status_change",
    ),
    url(r"^tag/list/$", views.TagList.as_view(), name="tag_list"),
    url(r"^tag/(?P<pk>[0-9]+)/$", views.TagDetail.as_view(), name="tag_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
