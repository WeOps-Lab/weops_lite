import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weops_lite.settings')
app = Celery('weops_lite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
