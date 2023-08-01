from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('new',views.new,name='new'),
    path('new/<str:pk>/',views.room,name="room")
]
