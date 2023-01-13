from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ReadOnlyField,
)
from django.urls import reverse

from .models import Event, Ticket


class EventSerializer(ModelSerializer):
    thumbnail = SerializerMethodField()

    def get_thumbnail(self, obj):
        # TODO: Make this absolute url instead of just path
        return reverse('event-thumbnail', args=[obj.id])

    class Meta:
        model = Event
        exclude = ('created', 'id')


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ('created', 'id')
        read_only_fields = ('owner',)
