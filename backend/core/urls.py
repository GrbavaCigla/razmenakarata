from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView

app_name = "core"

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("admin/", admin.site.urls),
    path("api/v1/", include("v1.urls", namespace="v1")),
]
