from django.db import models


class Timer(models.Model):
    """ Модель описывающая таймер """

    date = models.DateTimeField('Timestamp', auto_now_add=True)
    time = models.TimeField('Timer')
    event = models.CharField('Event', max_length=50)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Timer'
        verbose_name_plural = 'Timers'
