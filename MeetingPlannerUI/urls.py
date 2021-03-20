from django.urls import path
from .views import home, roomDetails, rooms


urlpatterns = [
    path('', home, name="home"),
    path('rooms', rooms, name="rooms"),
    path('room/<int:id>', roomDetails, name="roomDetails"),
]
