from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import EventViewset, TicketViewset

app_name = "api"

router = SimpleRouter()
router.register(r"events", EventViewset)

event_router = NestedSimpleRouter(router, r"events", lookup="event")
event_router.register(r"tickets", TicketViewset, basename="ticket")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(event_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token-obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
]
