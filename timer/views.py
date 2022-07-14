from datetime import timezone, datetime, timedelta, time

from django.shortcuts import render, redirect
from django.views import View

from timer.models import Timer


class WorkWithTimerView(View):

    def get(self, request):
        last_obj = Timer.objects.all().last()
        if last_obj:
            last_event = last_obj.event
            cur_timer = last_obj.time
            return render(request, 'index.html', {'event': last_event, 'timer': cur_timer})
        else:
            return render(request, 'index.html', {'event': 'Start'})


def button_click(request):
    last_obj = Timer.objects.all().last()
    if not last_obj:
        Timer.objects.create(time=time(), event='Start')
    else:
        minutes = 0
        start_time = last_obj.date
        time_zone = timezone(timedelta(hours=7))
        seconds = int((datetime.now(time_zone) - start_time).total_seconds())
        if seconds > 59:
            minutes = seconds // 60
            seconds %= 60
        cur_timer = time(minute=minutes, second=seconds)
        if last_obj.event == 'Start':
            Timer.objects.create(time=cur_timer, event='Stop')
        else:
            Timer.objects.create(time=cur_timer, event='Start')

    return redirect('home')
