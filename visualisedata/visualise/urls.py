from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('details',views.load_api,basename='details')
router.register('range',views.range,basename='range')
router.register('intensity',views.intensity,basename='range')

urlpatterns = [
    path('',include(router.urls)),
    path('home/',views.home.as_view())

    ]
