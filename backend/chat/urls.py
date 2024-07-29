from django.contrib import admin
from django.urls import path, include

from .views import ChatViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("chats", ChatViewset, basename="chat")

urlpatterns = [
    path("", include(router.urls)),
]
