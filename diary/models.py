#encoding:utf8
from django.db import models


class DatedModel(models.Model):
    added_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Entry(DatedModel):
    """
        Actor
    """
    comments = models.TextField(blank=False)

    def __str__(self):
        return u"Entry of {0}".format(self.added_date)

