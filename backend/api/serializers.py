from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SlugRelatedField,
)

from .models import Event, Ticket


class EventSerializer(ModelSerializer):
    thumbnail = HyperlinkedIdentityField(view_name="event-thumbnail")
    categories = SlugRelatedField(many=True, slug_field="name", read_only=True)
    packages = SlugRelatedField(many=True, slug_field="name", read_only=True)

    class Meta:
        model = Event
        exclude = ("created", "page")
        read_only_fields = ("categories", "packages")


class TicketSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Ticket
        exclude = ("created", "event")
        read_only_fields = ("owner",)
