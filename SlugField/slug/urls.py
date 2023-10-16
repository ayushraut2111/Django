from django.urls import path
from .views import *

urlpatterns = [
    path('student/<slug:pk>/',StudentView.as_view()),
    path('student/',StudentView.as_view()),
]