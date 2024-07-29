from datetime import datetime

from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    CharField,
    DateTimeField,
    ModelSerializer,
    PrimaryKeyRelatedField,
    Serializer,
)

from events.serializers import TicketSerializer
from .models import Chat

User = get_user_model()


class ChatSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(source="owner", read_only=True)

    def to_representation(self, instance):
        request = self.context.get("request")
        if request and request.user == instance.owner:
            self.fields["user"] = PrimaryKeyRelatedField(
                source="ticket.owner", read_only=True
            )

        self.fields["ticket"] = TicketSerializer(read_only=True)

        return super().to_representation(instance)

    class Meta:
        model = Chat
        fields = ("id", "user", "ticket")
        read_only_fields = ("id", "user")


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