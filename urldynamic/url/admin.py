from django.contrib import admin
from .models import student
# Register your models here.

# admin.site.register(student)

@admin.register(student)
class StudentRegister(admin.ModelAdmin):
    list_display=['id','name','roll','subject']
