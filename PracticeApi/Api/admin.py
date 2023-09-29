from django.contrib import admin
from .models import *


class StudentRegister(admin.ModelAdmin):
    list_display=['roll','name','subject']

admin.site.register(Student,StudentRegister)