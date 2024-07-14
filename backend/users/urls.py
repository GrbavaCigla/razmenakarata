from django.urls import path, include
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
    TokenVerifyView,
)

from .views import UserActivation


app_name = "auth"


urlpatterns = [
    path("", include("djoser.urls")),
    path(
        "auth/token/",
        TokenObtainPairView.as_view(),
        name="jwt-create",
    ),
    path(
        "auth/refresh/",
        TokenRefreshView.as_view(),
        name="jwt-refresh",
    ),
    path("auth/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
] + (
    [path("auth/activate/<str:uid>/<str:token>/", UserActivation.as_view())]
    if settings.INCLUDE_ACTIVATION_VIEW
    else []
)
