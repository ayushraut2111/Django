from django.urls import path,include
from .views import *

urlpatterns = [
    path('student/',ShowApi.as_view()),
    path('student/<pk>',ShowApi.as_view()),
    path('signup/',Signup.as_view())
]