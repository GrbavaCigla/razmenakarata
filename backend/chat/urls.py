from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import ChatViewset

router = SimpleRouter()
router.register("chats", ChatViewset, basename="chat")

urlpatterns = [
    path("", include(router.urls)),
]
