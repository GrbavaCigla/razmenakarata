import requests

from django.http import StreamingHttpResponse
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import action

from .models import Event, Ticket
from .serializers import EventSerializer, TicketSerializer


class EventViewset(ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(detail=True, renderer_classes=[StaticHTMLRenderer])
    def thumbnail(request, id):
        response = requests.get(Event.objects.get(id=id).thumbnail, stream=True)
        return StreamingHttpResponse(
            response.raw,
            content_type=response.headers.get('content-type'),
            status=response.status_code,
            reason=response.reason,
        )


class TicketViewset(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer