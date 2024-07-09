from django.db import models


class MonitoredSite(models.Model):
    url = models.URLField()
    check_interval = models.IntegerField()
    keyword = models.CharField(max_length=100)

    def __str__(self):
        return self.name
