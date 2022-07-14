from django.shortcuts import render
from django.views import View


class WorkWithTimerView(View):
    def get(self, request):
        context = {
            'a': 123,
            'b': 456,
            'c': 789,
            'd': 879,
            'button_text': 'Start'
        }
        return render(request, 'index.html', context=context)

    def post(self, request):
        print('123')
        return render(request, 'index.html', {'button_text': 'Stop'})
