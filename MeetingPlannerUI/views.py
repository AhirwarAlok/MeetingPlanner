from django.shortcuts import render
from .models import Room, Meeting


def home(request):
    roomCount = Room.objects.count()
    meetingCount = Meeting.objects.count()
    return render(request, "MeetingPlannerUI/home.html",
                  {"roomCount": roomCount, "meetingCount": meetingCount})


def rooms(request):
    rooms = Room.objects.all()
    return render(request, "MeetingPlannerUI/rooms.html", {"rooms": rooms})
