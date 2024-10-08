from django.db import models
from django.core.validators import MinValueValidator


class MonitoredSite(models.Model):
    url = models.URLField(unique=True)
    keyword = models.CharField(max_length=100)
    check_interval = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])  # Minimalna wartość 1 minuta
    last_content = models.TextField(blank=True, null=True)
    last_phrase_status = models.BooleanField(default=None, null=True, blank=True)

    def __str__(self):
        return self.url


class MonitoringResult(models.Model):
    site = models.ForeignKey(MonitoredSite, on_delete=models.CASCADE)
    result = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
