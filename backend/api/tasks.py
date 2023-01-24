import requests
from lxml import html

from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from rest_framework.response import Response

from .models import Event
from .utils import parse_date


HOST = 'http://new.gigstix.com'
XPATHS = {
    'grid': '//div[@class="gt-col"]',
    'name': './/div[@class="gt-title"]/a/text()',
    'city': './/div[@class="gt-location"]//a/text()',
    'thumbnail': './/div[@class="gt-image"]//img/@src',
    'date': './/div[@class="gt-date"]//span/text()',
    'categories': './/div[@class="gt-category"]//a/text()',
    'page': './/div[@class="gt-title"]/a/@href',

    'details-box': '//div[@class="gt-content-detail-box"]/ul',
    'date-suffix': '//div[@class="gt-content"]//div[@class="gt-inner"]/text()',
    'start-date': './/li[@class="gt-start-date"]',
    'end-date': './/li[@class="gt-end-date"]',
    'location': './/li[@class="gt-venue"]',
    'location-suffix': '//div[@class="gt-content"]//div[@class="gt-inner"]//a/text()',
    'packages': '//div[@class="gt-tickets-title"]/text()',
    'description': '//div[@class="gt-event-sections"]/div[1]//p/text()'
}


# TODO: Make this run every hour instead of every minute
# TODO: This is very error prone, add error handling
@db_periodic_task(crontab(minute='*/5'))
def refresh_db():
    resp = requests.get(HOST)
    if not resp.ok:
        return Response(resp.text, status=resp.status_code)

    events = []
    doc = html.document_fromstring(resp.text)
    for i, element in enumerate(doc.xpath(XPATHS['grid'])):
        data = {}
        data['name'] = element.xpath(XPATHS['name'])[0]
        data['city'] = element.xpath(XPATHS['city'])[0]
        data['thumbnail'] = element.xpath(XPATHS['thumbnail'])[0]
        # data['date'] = element.xpath(XPATHS['date'])[0]
        # data['categories'] = element.xpath(XPATHS['categories'])
        data['page'] = element.xpath(XPATHS['page'])[0]

        resp = requests.get(data['page'])
        if not resp.ok:
            return Response(resp.text, status=resp.status_code)
        doc = html.document_fromstring(resp.text)

        # TODO: Try catch this
        details_box = doc.xpath(XPATHS['details-box'])[0]
        data['start_date'] = parse_date(details_box.xpath(XPATHS['start-date'] + XPATHS['date-suffix'])[0])
        # TODO: Change this to something more reasonable
        try:
            data['end_date'] = parse_date(details_box.xpath(XPATHS['end-date'] + XPATHS['date-suffix'])[0])
        except Exception:
            pass
        try:
            data['location'] = details_box.xpath(XPATHS['location'] + XPATHS['location-suffix'])[0]
        except Exception:
            pass


        # data['packages'] = [i.strip() for i in doc.xpath(XPATHS['packages'])]
        data['description'] = ' '.join(doc.xpath(XPATHS['description']))

        events.append(Event(id=i, **data))
    
    # TODO: Delete this delete
    Event.objects.all().delete()

    Event.objects.bulk_create(events)