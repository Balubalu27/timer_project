from django.contrib import admin
from .models import Timer


@admin.register(Timer)
class TimerAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'event')
    ordering = ('id', )

