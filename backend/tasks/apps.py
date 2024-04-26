from django.apps import AppConfig
from django.utils.autoreload import autoreload_started
from pathlib import Path
from os import path


def watchdog(sender, *args, **kwargs):
    to_watch = ["tasks.py", "xpath.py", "utils.py"]

    for i in to_watch:
        sender.extra_files.add(Path(path.dirname(__file__)) / i)


class TasksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tasks"

    def ready(self):
        autoreload_started.connect(watchdog)
