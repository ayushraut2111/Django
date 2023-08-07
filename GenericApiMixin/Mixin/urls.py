from django.urls import path
from . import views

urlpatterns = [
    path('student/',views.make_api.as_view()),
    path('student/<int:pk>/',views.make_api_pk.as_view())
]
