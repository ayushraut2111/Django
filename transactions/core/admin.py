from django.contrib import admin
from core.models import Bank

@admin.register(Bank)
class Bankregister(admin.ModelAdmin):
    list_display=['name','amount']