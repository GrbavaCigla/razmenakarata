from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.urls import reverse

from .models import Event


class EventSerializer(ModelSerializer):
    thumbnail = SerializerMethodField()

    def get_thumbnail(self, obj):
        # TODO: Make this absolute url instead of just path
        return reverse('event-thumbnail', args=[obj.id])

    class Meta:
        model = Event
        exclude = ('created', 'id')
