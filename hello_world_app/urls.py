"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from hello_world_app import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('todoevent', views.event_view, name='event_view'), 
    
    path('todoevent/edit/<int:event_id>/', 
        views.edit_event, name='edit_event'),
    
    path('todoevent/delete/<int:event_id>/', 
        views.delete_event, name='delete_event'),
    
    path('register/', views.register_view, name='register_view'),
    
    path('login/', views.login_view, name='login_view'),
    
    path('logout/', views.logout_view, name='logout_view'),
    
    path('admin/', admin.site.urls),
    
    path('', views.index, name='home'),
]
