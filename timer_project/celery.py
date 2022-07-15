import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timer_project.settings')

app = Celery('timer')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_somth_0.5': {
        'task': 'timer.tasks.get_somth',
        'schedule': 0.5
    }
}

app.autodiscover_tasks()
