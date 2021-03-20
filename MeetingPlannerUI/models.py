from django.db import models
from datetime import time
from django.db.models.deletion import CASCADE


class Room(models.Model):
    roomNo = models.IntegerField()
    roomName = models.CharField(max_length=100)
    floorNumber = models.IntegerField(default=4)
    buildingName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.roomName}: Room {self.roomNo}, Floor {self.floorNumber}, {self.buildingName}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField(default=time(10))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=CASCADE)

    def __str__(self):
        return f"{self.title} scheduled on {self.time}, {self.date} at {self.room.roomName}"
