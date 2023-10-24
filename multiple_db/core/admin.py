from django.contrib import admin
from .models import Book, Student


@admin.register(Book)
class BookRegister(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Student)
class BookRegister(admin.ModelAdmin):
    list_display = ['id', 'name']
