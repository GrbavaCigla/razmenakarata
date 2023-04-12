from django.contrib.auth import get_user_model
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


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "password",
            "email",
            "email_confirmed",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                # TODO: Make this invisible to the public
                "write_only": True,
                "allow_null": False,
                "required": True,
                "allow_blank": False,
            },
            "first_name": {
                "allow_null": False,
                "required": True,
                "allow_blank": False,
            },
            "last_name": {
                "allow_null": False,
                "required": True,
                "allow_blank": False,
            },
            "email_confirmed": {"read_only": True},
            "id": {"read_only": True},
        }
