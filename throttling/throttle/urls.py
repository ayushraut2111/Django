from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('student',views.Student_api,basename="studentapi")


urlpatterns = [
    path('',include(router.urls)),
    path('login/',include('rest_framework.urls'))
]