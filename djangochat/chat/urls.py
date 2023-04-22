from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<str:room>/',views.room,name="room"),
    path('chatroom',views.chatroom,name="chatroom"),
    path('send',views.send,name="send"),
    path('getmessages/<str:room>/',views.getmessages,name="getmessages")
]
