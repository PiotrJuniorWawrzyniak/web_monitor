from django.contrib import admin
from .models import MonitoredSite


@admin.register(MonitoredSite)
class MonitoredSiteAdmin(admin.ModelAdmin):
    list_display = ('url', 'check_interval', 'keyword')
