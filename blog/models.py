# from django.db import models
#
#
# class MonitoredSite(models.Model):
#     url = models.URLField(unique=True)
#     check_interval = models.IntegerField(help_text="Interval in minutes")
#     search_phrase = models.CharField(max_length=255, blank=True, null=True)
#     last_checked = models.DateTimeField(blank=True, null=True)
#     last_changed = models.DateTimeField(blank=True, null=True)
#     phrase_found = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.url
#
#     class Meta:
#         verbose_name = "Monitored Page"
#         verbose_name_plural = "Monitored Pages"

# from django.db import models
#
#
# class MonitoredSite(models.Model):
#     url = models.URLField(unique=True)
#     check_interval = models.IntegerField(default=10)  # in minutes
#     search_phrase = models.CharField(max_length=255, blank=True, null=True)
#     last_checked = models.DateTimeField(blank=True, null=True)
#     phrase_found = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.url

# blog/models.py

# from django.db import models
#
#
# class MonitoredSite(models.Model):
#     name = models.CharField(max_length=100)
#     url = models.URLField()
#     check_interval = models.IntegerField()
#     keyword = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name

# blog/models.py

from django.db import models


class MonitoredSite(models.Model):
    # name = models.CharField(max_length=100)
    url = models.URLField()
    check_interval = models.IntegerField()
    keyword = models.CharField(max_length=100, default='default_keyword')

    def __str__(self):
        return self.name
