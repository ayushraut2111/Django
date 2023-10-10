from django.contrib import admin
from .models import *

class StudentAdminView(admin.ModelAdmin):
    list_display=['id','name','subject','roll']

admin.site.register(Student,StudentAdminView)

