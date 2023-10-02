from django.urls import path,include
from .views import *

urlpatterns = [
    path('signup/',Signup.as_view())
]