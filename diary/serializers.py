#coding:utf-8

from rest_framework import serializers
from rest_framework import pagination
from diary import models


class EntrySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='entry_detail', format='json')

    class Meta:
        model = models.Entry
        fields = (
            'id', 
            'url', 
            'comments', 
            'added_date', 
            'updated_date'
        )
