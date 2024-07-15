from django.db import models
from django.core.validators import MinValueValidator


class MonitoredSite(models.Model):
    url = models.URLField(unique=True)
    check_interval = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    keyword = models.CharField(max_length=100)
    last_content = models.TextField(blank=True, null=True)
    last_phrase_status = models.BooleanField(default=None, null=True, blank=True)

    def __str__(self):
        return self.url
