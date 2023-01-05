from rest_framework.decorators import api_view
from .utils import refresh_db


@api_view(["GET"])
def get_events(request):
    # TODO: Run periodicly instead of everytime
    return refresh_db()
