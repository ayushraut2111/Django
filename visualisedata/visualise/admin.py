from django.contrib import admin
from .models import details

@admin.register(details)
class DetailsRegister(admin.ModelAdmin):
    list_display=['id','intensity','topic','country']
