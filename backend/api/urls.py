from django.urls import path

from .views import get_proxy_image, EventDetail, EventList

urlpatterns = [
    path('events/', EventList.as_view(), name='event-list'),
    path('events/<int:id>/', EventDetail.as_view(), name='event-detail'),
    path('events/<int:id>/thumbnail', get_proxy_image, name='event-thumbnail')
]
