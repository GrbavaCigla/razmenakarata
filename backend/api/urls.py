from django.urls import path
from .views import get_events

urlpatterns = [
    path('events/', get_events)
]
