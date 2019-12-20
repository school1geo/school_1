# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Meaning
 
class MeaningAdmin(admin.ModelAdmin):
    list_display = ("word", "mean",)

admin.site.register(Meaning, MeaningAdmin)