from django import forms
from .models import ToDoEvent
      
class ToDoEventForm(forms.ModelForm):
    class Meta:
        model = ToDoEvent
        fields = ['EventTitle', 'EventDone', 'EventDescription', 'EventList']
    
    EventTitle = forms.CharField(label="Task Name:")
    EventDone = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), label="Mark as Done", required=False)
    EventDescription = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 50}), label="Description:", required=False)
    EventList = forms.CharField(label="To-Do List:", initial="default")

    