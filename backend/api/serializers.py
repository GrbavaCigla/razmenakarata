from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SlugRelatedField,
)

from .models import Event, Ticket


class EventSerializer(ModelSerializer):
    thumbnail = HyperlinkedIdentityField(view_name='event-thumbnail')

    class Meta:
        model = Event
        exclude = ('created', 'page')


class TicketSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Ticket
        exclude = ('created', 'event')
        read_only_fields = ('owner',)
