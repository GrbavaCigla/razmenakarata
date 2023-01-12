from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import get_proxy_image, EventDetail, EventList

urlpatterns = [
    path("events/", EventList.as_view(), name="event-list"),
    path("events/<int:id>/", EventDetail.as_view(), name="event-detail"),
    path("events/<int:id>/thumbnail", get_proxy_image, name="event-thumbnail"),
    path("token/", TokenObtainPairView.as_view(), name="token-obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]
