from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import MonitoredSite
from .tasks import check_sites
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json


@receiver(post_save, sender=MonitoredSite)
def monitor_site(sender, instance, **kwargs):
    # Konwersja minut na sekundy
    interval_in_seconds = max(int(instance.check_interval) * 60, 60)

    # Usuń stare zadanie, jeśli istnieje
    task_name = f"check_site_{instance.id}"
    old_task = PeriodicTask.objects.filter(name=task_name).first()
    if old_task:
        old_task.delete()

    # Utwórz lub zaktualizuj harmonogram
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=interval_in_seconds, period=IntervalSchedule.SECONDS
    )

    # Utwórz nowe zadanie cykliczne
    PeriodicTask.objects.create(
        interval=schedule,
        name=task_name,
        task="blog.tasks.check_sites",
        args=json.dumps([instance.id]),
    )

    # Sprawdzenie witryny po zapisaniu
    check_sites.delay(instance.id)


@receiver(post_delete, sender=MonitoredSite)
def delete_periodic_task(sender, instance, **kwargs):
    task_name = f"check_site_{instance.id}"
    try:
        task = PeriodicTask.objects.get(name=task_name)
        task.delete()
    except PeriodicTask.DoesNotExist:
        pass
