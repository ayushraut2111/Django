from django.urls import path
from . import views
urlpatterns = [
    path('student/',views.api_view.as_view()),
    path('student/<int:pk>/',views.api_view_pk.as_view()),
]
