from django.core.management.base import BaseCommand

from ...models import Category, Event, Package


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.delete_events()

    def delete_events(self):
        Event.objects.all().delete()
        Category.objects.all().delete()
        Package.objects.all().delete()
