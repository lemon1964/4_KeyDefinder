from django.db import models
from django.utils import timezone


class MessageFront(models.Model):
    user = models.CharField(max_length=30)
    date = models.DateField(default=timezone.now)
    screen = models.CharField(max_length=20)
    event = models.CharField(max_length=20)
    key = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'{self.user} - {self.date} - {self.screen} - {self.event} - {self.key}'


class UserKey(models.Model):
    user = models.CharField(max_length=30)
    keywisper = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user} - {self.keywisper}'




