from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if settings.DEBUG:
            self.delete_users()

    def delete_users(self):
        User.objects.all().delete()
