from django.urls import path,include
from . import views

urlpatterns = [
    path('student/',views.studentlist.as_view())
]