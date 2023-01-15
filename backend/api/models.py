from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    date = models.CharField(max_length=32)
    category = models.CharField(max_length=16)
    thumbnail = models.URLField()
    page = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']


class Ticket(models.Model):
    price = models.FloatField()
    event = models.ForeignKey(Event, models.CASCADE)
    owner = models.ForeignKey(User, models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
