import requests

from lxml import html
from celery.schedules import crontab

from .utils import scrape_page_data
from .xpaths import GRID_XPATH, LANDING_XPATHS, XPATHS
from events.models import Event, Package, Category
from core.celery import app

HOST = "http://new.gigstix.com"


@app.task(bind=True)
def fetch_events(self):
    resp = requests.get(HOST)
    # TODO: Check resp status

    packages = []
    categories = []

    doc = html.document_fromstring(resp.text)
    for element in doc.xpath(GRID_XPATH):
        data = scrape_page_data(element, LANDING_XPATHS)

        resp = requests.get(data["page"])
        # TODO: Check for resp status
        doc = html.document_fromstring(resp.text)
        data |= scrape_page_data(doc, XPATHS)

        _packages = data.get("packages", [])
        data.pop("packages", None)
        _categories = data.get("categories", [])
        data.pop("categories", None)

        event, _ = Event.objects.update_or_create(id=data["id"], defaults=data)

        packages += [Package(name=i, event=event) for i in _packages]
        categories += [Package(name=i, event=event) for i in _categories]

    Category.objects.all().delete()
    Package.objects.all().delete()

    Category.objects.bulk_create(categories)
    Package.objects.bulk_create(packages)


app.conf.beat_schedule = {
    "fetch_events": {
        "task": "tasks.tasks.fetch_events",
        "schedule": crontab(minute="*/5"),
    },
}
