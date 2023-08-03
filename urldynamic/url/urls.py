from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
   path('student',views.home,name="home"),
   path('index/<str:pk>/',views.index,name="url"),
   path('student/<int:pk>/',views.single,name="singledata"),
   path('studentdata',views.create_student,name="add")
]
