# coding:utf-8

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from diary import models


@login_required
def homepage(request):
    tags = models.Tag.objects.all()
    entries = models.Entry.objects.all().prefetch_related("tags", "status")
    return render(request, "index.html", {"tags": tags, "entries": entries})

