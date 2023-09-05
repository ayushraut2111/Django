from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class UserReg(admin.ModelAdmin):
    list_display=['username','name','phone']
