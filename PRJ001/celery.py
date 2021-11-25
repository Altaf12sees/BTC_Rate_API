import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PRJ001.settings')


app = Celery('APP001')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
