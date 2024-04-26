from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import action

from .models import Event, Ticket
from .serializers import EventSerializer, TicketSerializer
from users.permissions import IsOwnerOrReadOnly


class EventViewset(ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_fields = ["city", "location", "start_date", "end_date"]
    search_fields = ["name", "description"]
    ordering_fields = ["start_date", "end_date", "name"]

    @action(detail=True, renderer_classes=[StaticHTMLRenderer])
    def thumbnail(self, request, pk):
        # TODO: Check if jpg or some other type
        return HttpResponse(Event.objects.get(pk=pk).thumbnail, content_type="image/jpg")


class TicketViewset(ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Ticket.objects.filter(event=self.kwargs["event_pk"])

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, event_id=self.kwargs["event_pk"])


