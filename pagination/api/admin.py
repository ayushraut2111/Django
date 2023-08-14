from django.contrib import admin
from .models import student

@admin.register(student)
class StudentRegister(admin.ModelAdmin):
    list_display=['id','name']
