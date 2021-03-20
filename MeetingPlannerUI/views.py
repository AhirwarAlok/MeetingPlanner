from django.shortcuts import render
from .models import Room, Meeting


def home(request):
    roomCount = Room.objects.count()
    meetingCount = Meeting.objects.count()
    return render(request, 'MeetingPlannerUI/home.html',
                  {"roomCount": roomCount, "meetingCount": meetingCount})
