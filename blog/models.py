from django.db import models


class MonitoredSite(models.Model):
    url = models.URLField(unique=True)
    check_interval = models.IntegerField(help_text="Interval in minutes")
    search_phrase = models.CharField(max_length=255, blank=True, null=True)
    last_checked = models.DateTimeField(blank=True, null=True)
    last_changed = models.DateTimeField(blank=True, null=True)
    phrase_found = models.BooleanField(default=False)

    def __str__(self):
        return self.url
