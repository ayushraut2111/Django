from django.urls import path,include
from . import views

urlpatterns = [
    path('home',views.home.as_view()),
    path('makeuser/',views.MakeUser.as_view())
]