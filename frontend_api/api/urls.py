from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('student',views.studentapi)

urlpatterns = [
path('',include(router.urls)),
    path('home/',views.home.as_view()),
]
