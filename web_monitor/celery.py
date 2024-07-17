from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_monitor.settings')

app = Celery('web_monitor')

# Użycie ustawień Django w Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatyczne odkrywanie tasków we wszystkich aplikacjach Django
app.autodiscover_tasks()


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    from blog.models import MonitoredSite
    from blog.tasks import check_sites

    sites = MonitoredSite.objects.all()
    for site in sites:
        sender.add_periodic_task(
            site.check_interval * 60,  # Interwał w sekundach
            check_sites.s(site.id),
            name=f'check_site_{site.id}'
        )
