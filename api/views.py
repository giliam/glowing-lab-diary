#coding:utf-8

from django.shortcuts import render

from rest_framework import generics
from rest_framework import response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

from diary import models
from api import serializers


class EntryList(generics.ListCreateAPIView):
    queryset = models.Entry.objects.all()
    serializer_class = serializers.EntrySerializer


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Entry.objects.all()
    serializer_class = serializers.EntrySerializer


class TagList(generics.ListCreateAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return response.Response({
        'tag_list': reverse('tag_list', request=request, format=format),
        'entry_list': reverse('entry_list', request=request, format=format),
    })