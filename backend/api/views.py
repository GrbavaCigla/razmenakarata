import requests
from urllib.parse import urlparse
from rest_framework.decorators import api_view
from .utils import refresh_db
from django.http import StreamingHttpResponse


@api_view(['GET'])
def get_events(request):
    # TODO: Run periodicly instead of everytime
    return refresh_db()


def get_proxy_image(request):
    url = request.build_absolute_uri()
    parsed = urlparse(url)
    url = parsed._replace(netloc='www.gigstix.com', path=parsed.path[4:]).geturl()

    response = requests.get(url, stream=True)
    return StreamingHttpResponse(
        response.raw,
        content_type=response.headers.get('content-type'),
        status=response.status_code,
        reason=response.reason,
    )
