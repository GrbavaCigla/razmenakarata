from django.conf import settings
from django.urls import include, path
from djoser.views import TokenCreateView, TokenDestroyView

from .views import UserActivation

app_name = "auth"


urlpatterns = [
    path("", include("djoser.urls")),
    path("auth/login/", TokenCreateView.as_view(), name="login"),
    path("auth/logout/", TokenDestroyView.as_view(), name="logout"),
] + (
    [path("auth/activate/<str:uid>/<str:token>/", UserActivation.as_view())]
    if settings.INCLUDE_ACTIVATION_VIEW
    else []
)
