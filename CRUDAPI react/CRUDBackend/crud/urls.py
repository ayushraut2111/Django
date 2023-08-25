from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('student',views.Student_Api)

urlpatterns = [
    path('',include(router.urls))
    
]