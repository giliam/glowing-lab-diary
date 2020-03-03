from django.contrib import admin

import diary.models as models

# Register your models here.
admin.site.register(models.Entry)
admin.site.register(models.Tag)
admin.site.register(models.StatusEntry)
