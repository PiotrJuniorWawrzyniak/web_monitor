from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Ustawienie domyślnego modułu ustawień Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_monitor.settings')

app = Celery('web_monitor')

# Użycie ustawień Django w Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatyczne odkrywanie tasków we wszystkich aplikacjach Django
app.autodiscover_tasks()
