from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('pic',views.pic)

urlpatterns = [
    path('home/',views.home),
    path('',include(router.urls))

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)