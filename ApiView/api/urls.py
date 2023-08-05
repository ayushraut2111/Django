from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('student/',views.api_show),
    path('student/<int:pk>/',views.api_show)
]
