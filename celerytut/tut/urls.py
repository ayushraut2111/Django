from django.urls import path, include
from tut import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register('tutorial', views.TestViewset, basename='tut-viewset')


urlpatterns = [
    path('', include(router.urls)),
    path('tutorial/', views.list1, name='abc')

]
