from django.urls import path

from timer.views import WorkWithTimerView

urlpatterns = [
    path('', WorkWithTimerView.as_view(), name='home'),
]
