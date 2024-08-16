from django.db.models import Q

from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import ChatSerializer
from .models import Chat
from users.permissions import IsOwner


# TODO: filterset, search, ordering
class ChatViewset(
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Chat.objects.filter(
            Q(owner=self.request.user) | Q(ticket__owner=self.request.user)
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True)
    def messages(self, request, pk):
        return Response()
