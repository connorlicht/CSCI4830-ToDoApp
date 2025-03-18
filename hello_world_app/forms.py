from django import forms
from .models import Person
from .models import ToDoEvent
from .models import ToDoList

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['Name']
      
class ToDoEventForm(forms.ModelForm):
    class Meta:
        model = ToDoEvent
        fields = ['EventTitle', 'EventRank', 'EventDone']
    
class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['ListName', 'Events']