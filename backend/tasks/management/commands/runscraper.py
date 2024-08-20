import logging
import shlex
import subprocess

from django.core.management.base import BaseCommand
from django.utils import autoreload

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Command(BaseCommand):
    def handle(self, *args, **options):
        subprocess.call(
            shlex.split("celery -A core.celery call tasks.tasks.fetch_events")
        )
