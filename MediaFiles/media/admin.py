from django.contrib import admin
from .models import picture

@admin.register(picture)
class picRegister(admin.ModelAdmin):
    list_display=['id','name','image']
