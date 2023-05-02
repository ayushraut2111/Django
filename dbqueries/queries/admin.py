from django.contrib import admin

from .models import Room,Student,Course,Subject,Batch

admin.site.register(Room)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Batch)
