from django.contrib.auth import get_user_model
from django.db import models

from events.models import Ticket

User = get_user_model()


class Chat(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    class Meta:
        unique_together = (
            "ticket",
            "owner",
        )


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField(max_length=512)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
