from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MonitoredSite
from .tasks import check_sites


@receiver(post_save, sender=MonitoredSite)
def monitor_site(sender, instance, **kwargs):
    check_sites.delay(instance.id)
