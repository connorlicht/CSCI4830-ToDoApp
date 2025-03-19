from django.db import models
from django.contrib.auth.models import User
    
class ToDoEvent(models.Model):
    EventTitle = models.CharField(max_length=200)
    EventRank = models.IntegerField(default=-1)
    EventDone = models.BooleanField(default=False);
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
class ToDoList(models.Model):
    ListName = models.CharField(max_length=200)
    Events = models.ManyToManyField(ToDoEvent)