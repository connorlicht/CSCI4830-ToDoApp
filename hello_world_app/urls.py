from django.urls import path
from hello_world_app import views
from django.contrib import admin

urlpatterns = [

    path('todoevent/<str:eventList>/', views.event_view, name='event_view'),
    
    # path('searchevent/<str:eventList>/', views.search_event, name='search_event'),
    
    path('selecteventlist', views.select_event_list, name='select_event_list'),
    
    path('todoevent/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    
    path('todoevent/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    
    path('register/', views.register_view, name='register_view'),
    
    path('login/', views.login_view, name='login_view'),
    
    path('logout/', views.logout_view, name='logout_view'),
    
    path('admin/', admin.site.urls),
    
    path('', views.index, name='home'),
]
