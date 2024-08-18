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
    messages = models.JSONField(null=False, blank=False, default=list)

    class Meta:
        unique_together = (
            "ticket",
            "owner",
        )
