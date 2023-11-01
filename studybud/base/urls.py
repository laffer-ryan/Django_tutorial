from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name="room"),
    path('room_form/', views.createRoom, name="create-room"),
    path('room_form/<str:pk>/', views.updateRoom, name="update-room"),
    path('room_form/<str:pk>', views.deleteRoom, name="delete-room"),
]