#coding:utf-8

from django.shortcuts import render

from diary import models

def homepage(request):
    tags = models.Tag.objects.all()
    entries = models.Entry.objects.all()
    return render(request, 'index.html', {
        "tags": tags,
        "entries": entries,
    })