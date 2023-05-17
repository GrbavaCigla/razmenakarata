from django.urls import path, include
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import EventViewset, TicketViewset, UserDetail

app_name = "api"

router = SimpleRouter()
router.register(r"events", EventViewset)

event_router = NestedSimpleRouter(router, r"events", lookup="event")
event_router.register(r"tickets", TicketViewset, basename="ticket")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(event_router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
]
