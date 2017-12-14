#encoding:utf8
from django.db import models


class DatedModel(models.Model):
    added_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(DatedModel):
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return u"#{0}".format(self.name)


class Entry(DatedModel):
    """
        Entry
    """
    comments = models.TextField(blank=False)
    tags = models.ManyToManyField(Tag, related_name="entries")

    def __str__(self):
        return u"Entry of {0}".format(self.added_date)

