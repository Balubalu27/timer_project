from django.shortcuts import render
from django.views import View

from timer.models import Timer


class WorkWithTimerView(View):

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        print('123')
        return render(request, 'index.html')
