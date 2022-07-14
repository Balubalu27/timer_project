import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timer_project.settings')

app = Celery('timer')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_somth_2s': {
        'task': 'timer.tasks.get_somth',
        'schedule': 2.0
    }
}

app.autodiscover_tasks()
