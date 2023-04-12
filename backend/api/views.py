from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView

from .models import Event, Ticket
from .permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer, TicketSerializer, UserSerializer


class EventViewset(ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_fields = ["city", "location", "start_date", "end_date"]
    search_fields = ["name", "description"]
    ordering_fields = ["start_date", "end_date", "name"]

    @action(detail=True, renderer_classes=[StaticHTMLRenderer])
    def thumbnail(self, request, pk):
        return HttpResponse(Event.objects.get(pk=pk).thumbnail)


class TicketViewset(ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Ticket.objects.filter(event=self.kwargs["event_pk"])

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, event_id=self.kwargs["event_pk"])


class UserDetail(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer