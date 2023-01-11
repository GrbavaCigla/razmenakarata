from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    date = models.CharField(max_length=32)
    category = models.CharField(max_length=16)
    thumbnail = models.URLField()
    page = models.URLField()
    created = models.DateTimeField(auto_now_add=True)