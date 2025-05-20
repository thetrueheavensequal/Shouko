import os
from dotenv import load_dotenv
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Shouko.settings')
app = Celery('Shouko')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()