from django.db import models


class Person(models.Model):
    Name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Name
    
class ToDoEvent(models.Model):
    EventTitle = models.CharField(max_length=200)
    EventRank = models.IntegerField(default=-1)
    EventDone = models.BooleanField(default=False);
    
class ToDoList(models.Model):
    ListName = models.CharField(max_length=200)
    Events = models.ManyToManyField(ToDoEvent)