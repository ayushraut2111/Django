from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('student',views.make_api,basename="studentapi")

urlpatterns = [
    path('',include(router.urls))
]