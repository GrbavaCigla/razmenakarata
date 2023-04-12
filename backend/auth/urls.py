from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserRegister

app_name = "auth"

urlpatterns = [
    # TODO: Rename this route
    path("register/", UserRegister.as_view(), name="user-register"),
    path("token/", TokenObtainPairView.as_view(), name="token-obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]
