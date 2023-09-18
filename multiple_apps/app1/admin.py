from django.contrib import admin

from .models import User1,People

@admin.register(User1)
class UserReg(admin.ModelAdmin):
    list_display=['id','username']
@admin.register(People)
class PeopleReg(admin.ModelAdmin):
    list_display=['id','name','user']
