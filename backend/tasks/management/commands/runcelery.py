import logging
import shlex
import subprocess

from django.core.management.base import BaseCommand
from django.utils import autoreload

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def restart_celery():
    # subprocess.call(shlex.split("pkill celery"))
    subprocess.call(
        shlex.split("celery -A core.celery worker -n celery@celery -l debug")
    )


class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info("Starting development celery worker with autoreload...")
        autoreload.run_with_reloader(restart_celery)
