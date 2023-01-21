from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    location = models.CharField(max_length=64)
    # TODO: Change this to proper date field
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
    amount = models.PositiveSmallIntegerField(default=1)
    online = models.BooleanField()
    packet = models.CharField(max_length=128)
    owner = models.ForeignKey(User, models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
