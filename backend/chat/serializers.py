from datetime import datetime

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.serializers import (
    CharField,
    DateTimeField,
    ModelSerializer,
    PrimaryKeyRelatedField,
    Serializer,
    CurrentUserDefault,
)

from events.serializers import TicketSerializer
from .models import Chat

User = get_user_model()


class ChatSerializer(ModelSerializer):
    owner = PrimaryKeyRelatedField(default=CurrentUserDefault(), read_only=True)
    user = PrimaryKeyRelatedField(source="owner", read_only=True)

    def to_representation(self, instance):
        request = self.context.get("request")
        if request and request.user == instance.owner:
            self.fields["user"] = PrimaryKeyRelatedField(
                source="ticket.owner", read_only=True
            )

        self.fields["ticket"] = TicketSerializer(read_only=True)
        del self.fields["owner"]

        return super().to_representation(instance)

    def validate_ticket(self, ticket):
        request = self.context.get("request")
        if request and request.method == "POST" and ticket.owner == request.user:
            raise ValidationError(
                _("You cannot purchase your ticket."),
                code="identical_users",
            )

        return ticket

    class Meta:
        model = Chat
        fields = ("id", "user", "ticket", "owner")
        read_only_fields = ("id", "user", "owner")


class MessageSerializer(Serializer):
    text = CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        max_length=256,
    )
    timestamp = DateTimeField(
        allow_null=False,
        default=datetime.now,
    )
    owner = PrimaryKeyRelatedField(
        queryset=User.objects.all(),
    )
