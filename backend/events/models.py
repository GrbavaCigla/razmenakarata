from django.conf import settings
from django.db import models

from sorl.thumbnail import ImageField


class Event(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    city = models.CharField(max_length=32)
    location = models.CharField(max_length=64, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    thumbnail = ImageField(upload_to="event/thumbnail")
    page = models.URLField()

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["start_date"]


class Package(models.Model):
    name = models.CharField(max_length=64)
    event = models.ForeignKey(Event, related_name="packages", on_delete=models.CASCADE)


class Ticket(models.Model):
    price = models.PositiveIntegerField()
    event = models.ForeignKey(Event, models.CASCADE)
    amount = models.PositiveSmallIntegerField(default=1)
    online = models.BooleanField()
    package = models.ForeignKey(Package, models.CASCADE, blank=False, null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["price"]


class Category(models.Model):
    name = models.CharField(max_length=16)
    event = models.ForeignKey(
        Event, related_name="categories", on_delete=models.CASCADE
    )
