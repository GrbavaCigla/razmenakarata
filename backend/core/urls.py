from django.contrib import admin
from django.urls import path, include

app_name = "core"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("v1.urls", namespace="v1")),
]
