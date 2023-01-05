from rest_framework.response import Response
from urllib.parse import urlparse
import requests
from lxml import html
from .models import Event
from .serializers import EventSerializer


def refresh_db():
    resp = requests.get("http://www.gigstix.com/")
    if not resp.ok:
        return Response(resp.text, status=resp.status_code)

    Event.objects.all().delete()

    doc = html.document_fromstring(resp.text)
    for i, element in enumerate(doc.xpath('//table[@class="minifp"]/tr/td')):
        name, date, location = element.xpath(
            'span[@class="minifp-introtitle"]/a/text()'
        )
        etype = element.xpath('span[@class="minifp-anotherlinks"]/a/text()')[0]
        thumbnail = urlparse(element.xpath("a/img/@src")[0])
        # TODO: Unhardcode this
        thumbnail = thumbnail._replace(
            netloc="127.0.0.1:8000", path="api/" + thumbnail.path
        )

        name = str(name).strip()
        date = str(date).strip()
        location = str(location).strip()
        etype = str(etype).strip()
        thumbnail = thumbnail.geturl()

        print(thumbnail)

        Event(
            id=i,
            name=name,
            location=location,
            date=date,
            etype=etype,
            thumbnail=thumbnail,
        ).save()

    return Response(EventSerializer(Event.objects.all(), many=True).data)
