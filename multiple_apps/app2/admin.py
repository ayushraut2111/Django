from django.contrib import admin

from .models import User2

@admin.register(User2)
class UserReg(admin.ModelAdmin):
    list_display=['id','username']
