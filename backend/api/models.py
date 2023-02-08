from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    city = models.CharField(max_length=32)
    location = models.CharField(max_length=64, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    thumbnail = models.URLField()
    page = models.URLField()

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["start_date"]


class Ticket(models.Model):
    price = models.FloatField()
    event = models.ForeignKey(Event, models.CASCADE)
    amount = models.PositiveSmallIntegerField(default=1)
    online = models.BooleanField()
    package = models.CharField(max_length=128)
    owner = models.ForeignKey(User, models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["price"]


class Package(models.Model):
    name = models.CharField(max_length=64)
    event = models.ForeignKey(Event, related_name='packages', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=16)
    event = models.ForeignKey(Event, related_name='categories', on_delete=models.CASCADE)
