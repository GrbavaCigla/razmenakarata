from django.urls import path, include

app_name = "v1"

urlpatterns = [
    path("auth/", include("users.urls")),
    path("", include("events.urls")),
]
