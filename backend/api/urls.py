from django.urls import path, re_path
from .views import get_events, get_proxy_image

urlpatterns = [
    path('events/', get_events),
    re_path('^images/', get_proxy_image)
]
