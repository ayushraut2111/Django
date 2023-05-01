from django.contrib import admin

from .models import Room,Student,Course

admin.site.register(Room)
admin.site.register(Course)
admin.site.register(Student)
