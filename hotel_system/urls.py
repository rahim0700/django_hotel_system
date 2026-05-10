"""
URL configuration for hotel_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from bookings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.room_list, name='home'),
    path('register/', views.register_guest, name='register_guest'),
    path('check-in/', views.check_in_guest, name='check_in'),
    path('guest/<int:guest_id>/', views.guest_detail, name='guest_detail'),
    path('check-out/<int:booking_id>/', views.check_out_guest, name='check_out_guest'),
]
