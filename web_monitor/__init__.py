from __future__ import absolute_import, unicode_literals

# Import Celery aplikacji
from .celery import app as celery_app

__all__ = ('celery_app',)
