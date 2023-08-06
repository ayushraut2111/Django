from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home.as_view()),
    path('student/',views.api_show.as_view()),
    path('student/<int:pk>/',views.api_show.as_view())
]