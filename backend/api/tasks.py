import requests
from lxml import html

from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from rest_framework.response import Response

from .models import Event
from .utils import split_list


HOST = 'http://www.gigstix.com'
XPATHS = {
    'title': 'span[@class="minifp-introtitle"]/a/text()',
    'category': 'span[@class="minifp-anotherlinks"]/a/text()',
    'thumbnail': 'a/img/@src',
    'page': 'div[@class="minifp-full-link-wrp"]/a/@href',
    'headers': '//div[@id="page"]/p[@class="sectiontableheader"]//text()',
    'texts': '//div[@id="page"]/p//text()',
}


# TODO: Visit every page
# TODO: Make this run every hour instead of every minutec
@db_periodic_task(crontab(minute='*/5'))
def refresh_db():
    resp = requests.get(HOST)
    if not resp.ok:
        return Response(resp.text, status=resp.status_code)

    # TODO: Delete this delete
    Event.objects.all().delete()

    events = []
    doc = html.document_fromstring(resp.text)
    for i, element in enumerate(doc.xpath('//table[@class="minifp"]/tr/td')):
        data = {}
        data['name'], data['date'], data['location'] = element.xpath(XPATHS['title'])
        data['category'] = element.xpath(XPATHS['category'])[0]
        data['thumbnail'] = element.xpath(XPATHS['thumbnail'])[0]
        data['page'] = HOST + element.xpath(XPATHS['page'])[0]
        data = {k: str(v).strip() for k, v in data.items()}

        resp = requests.get(data['page'])
        doc = html.document_fromstring(resp.text)

        headers = doc.xpath(XPATHS['headers'])
        texts = [i.strip() for i in doc.xpath(XPATHS['texts']) if i.strip()]
        page = split_list(texts, headers)
        
        data['description'] = ' '.join(page[0][1:])
        data['location'] = page[1][0]
    
        events.append(Event(**data))

    Event.objects.bulk_create(events)