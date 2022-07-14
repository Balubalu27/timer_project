import json

from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

from timer.models import Timer

channel_layer = get_channel_layer()


@shared_task()
def get_somth():
    timer_objects = list(Timer.objects.all().values())
    text = json.dumps(timer_objects, default=str)
    async_to_sync(channel_layer.group_send)('timer', {'type': 'send_new_data', 'text': text})
