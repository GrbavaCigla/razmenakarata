import requests

from django.http import StreamingHttpResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter

from .models import Event, Ticket
from .permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer, TicketSerializer


class EventViewset(ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # TODO: For some reason this ignores Serializer excludes
    filterset_fields = "__all__"
    search_fields = ['name', 'description']
    ordering_fields = "__all__"

    @action(detail=True, renderer_classes=[StaticHTMLRenderer])
    def thumbnail(self, request, pk):
        response = requests.get(Event.objects.get(pk=pk).thumbnail, stream=True)
        return StreamingHttpResponse(
            response.raw,
            content_type=response.headers.get("content-type"),
            status=response.status_code,
            reason=response.reason,
        )


class TicketViewset(ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Ticket.objects.filter(event=self.kwargs["event_pk"])

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, event_id=self.kwargs["event_pk"])
