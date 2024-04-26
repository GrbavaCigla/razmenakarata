from django.urls import path, include

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
        "token/",
        TokenObtainPairView.as_view(),
        name="jwt-create",
    ),
    path(
        "refresh/",
        TokenRefreshView.as_view(),
        name="jwt-refresh",
    ),
    path("verify/", TokenVerifyView.as_view(), name="jwt-verify"),
    path("activate/<str:uid>/<str:token>/", UserActivation.as_view()),
]
