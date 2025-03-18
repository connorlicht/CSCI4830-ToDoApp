from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import ToDoEvent
from .forms import ToDoEventForm

def index(request):
    return render(request, 'index_hello.html')

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_view')
    else:
        form = UserCreationForm()
        
    return render(request, "users/register.html", {"form" : form})

def event_view(request):
    events = ToDoEvent.objects.all()
    
    if request.method == "POST":
        form = ToDoEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_view')
    else:
        form = ToDoEventForm()
            
    return render(request, 'event_list.html', {'form': form, 'events': events})

def edit_event(request, event_id):
    event = get_object_or_404(ToDoEvent, id=event_id)
    
    if request.method == "POST":
        form = ToDoEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            print("test")
            return redirect('event_view')
    else:
        form = ToDoEventForm(instance=event)
            
    return render(request, 'event_edit.html', {'form': form, 'event': event})

def delete_event(request, event_id):
    # Delete a specific score
    event = get_object_or_404(ToDoEvent, id=event_id)
    event.delete()
    return redirect('event_view')
            
