from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView

app_name = "v1"

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(api_version="v1"), name="schema"),
    path("", include("users.urls")),
    path("", include("events.urls")),
    path("", include("chat.urls")),
]
