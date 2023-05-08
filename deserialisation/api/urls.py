from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('stucreate',views.stucreate,name="create")
]
