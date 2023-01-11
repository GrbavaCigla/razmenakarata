import requests

from django.http import StreamingHttpResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Event
from .serializers import EventSerializer


class EventList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


def get_proxy_image(request, id):
    response = requests.get(Event.objects.get(id=id).thumbnail, stream=True)
    return StreamingHttpResponse(
        response.raw,
        content_type=response.headers.get('content-type'),
        status=response.status_code,
        reason=response.reason,
    )
