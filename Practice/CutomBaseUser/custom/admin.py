from django.contrib import admin

from .models import CustomUser

class CustomUserRegister(admin.ModelAdmin):
    list_display=['phone','username','is_superuser']

admin.site.register(CustomUser,CustomUserRegister)
