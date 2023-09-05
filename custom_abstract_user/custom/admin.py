from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class userregister(admin.ModelAdmin):
    list_display=['email','phone']
