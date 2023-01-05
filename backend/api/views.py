from rest_framework.decorators import api_view
from .utils import refresh_db


@api_view(["GET"])
def get_events(request):
    # TODO: Make this run periodicly
    return refresh_db()
