from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()

router.register('student',StudentView,basename='student-view')

urlpatterns = [
    path('',include(router.urls))
]