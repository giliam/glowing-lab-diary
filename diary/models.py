# encoding:utf8
from django.db import models


class DatedModel(models.Model):
    added_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(DatedModel):
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return f"#{self.name}"


class StatusEntry(DatedModel):
    content = models.CharField(max_length=150, blank=False, null=False)
    order = models.PositiveIntegerField(default=0)
    css_class = models.CharField(max_length=150, default="btn-primary")

    def __str__(self):
        return str(self.content)


class Entry(DatedModel):
    """
        Entry
    """

    comments = models.TextField(blank=False)
    tags = models.ManyToManyField(Tag, related_name="entries")
    status = models.ForeignKey(
        StatusEntry, on_delete=models.SET_NULL, null=True, related_name="entries"
    )

    def __str__(self):
        return f"Entry of {self.added_date}"

