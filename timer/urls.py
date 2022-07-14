from django.urls import path

from timer.views import WorkWithTimerView, button_click

urlpatterns = [
    path('', WorkWithTimerView.as_view(), name='home'),
    path('button/', button_click, name='button'),
]
