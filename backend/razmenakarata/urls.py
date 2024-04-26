from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("schema/", SpectacularAPIView.as_view()),
    path("api/v1/", include("core.urls", namespace="v1")),
]
