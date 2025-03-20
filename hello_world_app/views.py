from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import ToDoEvent
from .forms import ToDoEventForm
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index_hello.html')

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('event_view')
    else:
        form = UserCreationForm()
        
    return render(request, "users/register.html", {"form" : form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("select_event_list")
    
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else: 
                return redirect("select_event_list")
    else:
        form = AuthenticationForm()
        
    return render(request, "users/login.html", {"form" : form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

@login_required(login_url="/login")
def event_view(request, eventList):
    events = ToDoEvent.objects.filter(EventList=eventList, owner=request.user)
    p = Paginator(ToDoEvent.objects.filter(EventList=eventList, owner=request.user), 8)
    page = request.GET.get('page')
    pagedEvents = p.get_page(page)
    
    if request.method == "POST":
        form = ToDoEventForm(request.POST)
        if form.is_valid():
            newevent = form.save(commit=False)
            newevent.owner = request.user
            newevent.save()
            return redirect('event_view', eventList)
    else:
        form = ToDoEventForm()

    return render(request, 'event_list.html', {'form': form, 'events': events, 'eventList': eventList, 'pagedEvents': pagedEvents})


@login_required(login_url="/login")
def edit_event(request, event_id):
    event = get_object_or_404(ToDoEvent, id=event_id)
    
    if request.method == "POST":
        form = ToDoEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            print("test")
            return redirect('event_view', event.EventList)
    else:
        form = ToDoEventForm(instance=event)
            
    return render(request, 'event_edit.html', {'form': form, 'event': event})

@login_required(login_url="/login")
def delete_event(request, event_id):
    event = get_object_or_404(ToDoEvent, id=event_id)
    event.delete()
    return redirect('event_view', event.EventList)

@login_required(login_url="/login")
def select_event_list(request):
    events = ToDoEvent.objects.filter(owner=request.user)
    eventLists = events.values('EventList').distinct()
    
    print(eventLists)
    if eventLists.count() <= 0:
        ToDoEvent.objects.create(EventTitle="example", EventDescription="example", owner=request.user, EventList="default")

    if request.method == "POST":
        selected_event_list = request.POST.get('eventList')
        if selected_event_list:
            return redirect('event_view', eventList=selected_event_list)
        else:
            return redirect('select_event_list')
    
    return render(request, 'select_event_list.html', {'eventLists': eventLists})



            
