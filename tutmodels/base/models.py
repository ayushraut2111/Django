from django.db import models

class feature(models.Model):
    name=models.CharField(max_length=250)
    details=models.CharField(max_length=250)
