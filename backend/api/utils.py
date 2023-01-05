from rest_framework.response import Response
import requests
from lxml import html
from .models import Event
from .serializers import EventSerializer


def refresh_db():
    resp = requests.get('http://www.gigstix.com/')
    if not resp.ok:
        return Response(resp.text, status=resp.status_code)

    Event.objects.all().delete()

    doc = html.document_fromstring(resp.text)
    for i in doc.xpath('//table[@class="minifp"]/tr/td'):
        name, date, location = i.xpath('span[@class="minifp-introtitle"]/a/text()')
        etype = i.xpath('span[@class="minifp-anotherlinks"]/a/text()')[0]
        thumbnail = i.xpath('a/img/@src')[0]

        name = str(name).strip()
        date = str(date).strip()
        location = str(location).strip()
        etype = str(etype).strip()
        thumbnail = str(thumbnail).strip()

        Event(name=name, location=location, date=date, etype=etype, thumbnail=thumbnail).save()

    return Response(EventSerializer(Event.objects.all(), many=True).data)