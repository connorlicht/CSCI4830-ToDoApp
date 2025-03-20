from django.db import models
from django.contrib.auth.models import User
    
class ToDoEvent(models.Model):
    EventTitle = models.CharField(max_length=200)
    EventDone = models.BooleanField(default=False);
    EventDescription = models.TextField(max_length=1000, default="")
    EventList = models.CharField(max_length=200, default="default")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
class ToDoList(models.Model):
    ListName = models.CharField(max_length=200)
    Events = models.ManyToManyField(ToDoEvent)