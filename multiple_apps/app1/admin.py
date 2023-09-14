from django.contrib import admin

from .models import User1

@admin.register(User1)
class UserReg(admin.ModelAdmin):
    list_display=['id','username']
