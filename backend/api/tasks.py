import requests
from lxml import html

from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from rest_framework.response import Response

from .models import Event


# TODO: Visit every page
# TODO: Make this run every hour instead of every minutec
@db_periodic_task(crontab())
def refresh_db():
    resp = requests.get('http://www.gigstix.com/')
    if not resp.ok:
        return Response(resp.text, status=resp.status_code)

    # TODO: Delete this delete
    Event.objects.all().delete()

    doc = html.document_fromstring(resp.text)
    for i, element in enumerate(doc.xpath('//table[@class="minifp"]/tr/td')):
        name, date, location = element.xpath(
            'span[@class="minifp-introtitle"]/a/text()'
        )
        category = element.xpath('span[@class="minifp-anotherlinks"]/a/text()')[0]
        thumbnail = element.xpath('a/img/@src')[0]

        name = str(name).strip()
        date = str(date).strip()
        location = str(location).strip()
        category = str(category).strip()
        thumbnail = str(thumbnail)

        Event(
            id=i,
            name=name,
            location=location,
            date=date,
            category=category,
            thumbnail=thumbnail,
        ).save()
