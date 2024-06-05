from django.contrib import admin
from DB.models import Student
# Register your models here.
@admin.register(Student)
class StudentRegister(admin.ModelAdmin):
    list_display=["name"]