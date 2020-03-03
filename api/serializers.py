# coding:utf-8

from rest_framework import serializers
from rest_framework import pagination

from diary import models


class EntrySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="entry_detail", format="json")

    class Meta:
        model = models.Entry
        fields = (
            "id",
            "url",
            "comments",
            "tags",
            "status",
            "added_date",
            "updated_date",
        )


class TagSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="tag_detail", format="json")

    class Meta:
        model = models.Tag
        fields = ("id", "url", "name", "added_date", "updated_date")


class StatusEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StatusEntry
        fields = ("id", "content", "order", "css_class")
