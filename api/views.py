# coding:utf-8

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.shortcuts import render, get_object_or_404
from django.utils.formats import date_format
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, permissions, response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

from diary import models
from api import serializers


class EntryList(generics.ListCreateAPIView):
    queryset = models.Entry.objects.all()
    serializer_class = serializers.EntrySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_context(self):
        context = super(EntryList, self).get_serializer_context()
        print(context)
        return context


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Entry.objects.all()
    serializer_class = serializers.EntrySerializer
    permission_classes = (permissions.IsAuthenticated,)


class StatusEntryList(generics.ListAPIView):
    queryset = models.StatusEntry.objects.all()
    serializer_class = serializers.StatusEntrySerializer
    permission_classes = (permissions.IsAuthenticated,)


class TagList(generics.ListCreateAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = (permissions.IsAuthenticated,)


@api_view(["GET"])
@login_required
def api_root(request, format=None):
    return response.Response(
        {
            "tag_list": reverse("tag_list", request=request, format=format),
            "entry_list": reverse("entry_list", request=request, format=format),
            "status_list": reverse("status_list", request=request, format=format),
        }
    )


@api_view(["GET"])
@login_required
def change_status(request, entry_pk):
    entry = get_object_or_404(
        models.Entry.objects.prefetch_related("status"), id=int(entry_pk)
    )
    max_status = int(models.StatusEntry.objects.aggregate(Max("order"))["order__max"])
    status = get_object_or_404(
        models.StatusEntry, order=(entry.status.order + 1) % (max_status + 1)
    )
    entry.status = status
    entry.save()

    serializer = serializers.StatusEntrySerializer(status)
    return response.Response(serializer.data)


@api_view(["GET"])
@login_required
def entry_remove_tag(request, entry_pk, tag_pk):
    entry = get_object_or_404(
        models.Entry.objects.prefetch_related("status"),
        id=int(entry_pk),
        tags__in=tag_pk,
    )
    entry.tags.remove(tag_pk)
    return response.Response({})


@api_view(["GET"])
@login_required
def entry_add_tag(request, entry_pk, tag_pk):
    entry = get_object_or_404(
        models.Entry.objects.prefetch_related("status"), id=int(entry_pk)
    )
    tag = get_object_or_404(models.Tag, id=int(tag_pk))
    entry.tags.add(tag)
    return response.Response({})


@api_view(["POST"])
@login_required
def entry_new(request):
    if request.method == "POST":
        entry_content = request.data["entry"].strip()
        entry_tags = request.data["tags"]
        if len(entry_content) > 0:
            entry = models.Entry()
            entry.comments = entry_content
            entry.status = get_object_or_404(models.StatusEntry, order=0)
            entry.save()
            if len(entry_tags) > 0:
                tags = models.Tag.objects.filter(id__in=entry_tags)
                entry.tags.add(*tags)

            entry.status_dict = {
                "content": entry.status.content,
                "css_class": entry.status.css_class,
            }
            entry.added_date = date_format(entry.added_date, settings.DATETIME_FORMAT)
            serializer = serializers.EntryNewSerializer(entry)
            return response.Response(serializer.data)
    return response.Response({})
