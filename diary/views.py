#coding:utf-8

from django.shortcuts import render

from rest_framework import generics
from rest_framework.decorators import api_view

from diary import models
from diary import serializers


class EntryList(generics.ListCreateAPIView):
    queryset = models.Entry.objects.all()
    serializer_class = serializers.EntrySerializer


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Entry.objects.all()
    serializer_class = serializers.EntrySerializer


def api_root(request):
    return render(request, "index.html", {})