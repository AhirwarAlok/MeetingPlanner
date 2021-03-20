from django.shortcuts import get_object_or_404, render
from .models import Room, Meeting


def home(request):
    roomCount = Room.objects.count()
    meetingCount = Meeting.objects.count()
    return render(request, "MeetingPlannerUI/home.html",
                  {"roomCount": roomCount, "meetingCount": meetingCount})


def rooms(request):
    rooms = Room.objects.all()
    return render(request, "MeetingPlannerUI/rooms.html", {"rooms": rooms})


def roomDetails(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, "MeetingPlannerUI/roomDetails.html", {"room": room})


def meetings(request):
    meetings = Meeting.objects.all()
    return render(request, "MeetingPlannerUI/meetings.html", {"meetings": meetings})


def meetingDetails(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "MeetingPlannerUI/meetingDetails.html", {"meeting": meeting})
