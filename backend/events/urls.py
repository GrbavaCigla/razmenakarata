from django.urls import include, path
from rest_framework_nested.routers import NestedSimpleRouter, SimpleRouter

from .views import EventViewset, TicketViewset

router = SimpleRouter()
router.register(r"events", EventViewset)

event_router = NestedSimpleRouter(router, r"events", lookup="event")
event_router.register(r"tickets", TicketViewset, basename="ticket")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(event_router.urls)),
]
