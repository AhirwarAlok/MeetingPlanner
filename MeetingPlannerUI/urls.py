from django.urls import path
from .views import default, home, meetingDetails, meetings, roomDetails, rooms


urlpatterns = [
    path("", default, name="default"),
    path("home", home, name="home"),
    path("rooms", rooms, name="rooms"),
    path("room/<int:id>", roomDetails, name="roomDetails"),
    path("meetings", meetings, name="meetings"),
    path("meeting/<int:id>", meetingDetails, name="meetingDetails"),
]
