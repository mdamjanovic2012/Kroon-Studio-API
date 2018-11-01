from __future__ import absolute_import, unicode_literals
import os

os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KroonStudioPDT.settings')

app = Celery('KroonStudioPDT', broker="redis://127.0.0.1:6379/1")

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self))
