from django.contrib import admin

from .models import Product,Brand,student,course

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(student)
admin.site.register(course)
