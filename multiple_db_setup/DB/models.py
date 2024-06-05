from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    db_name = settings.APPOINTMENT_DB

    class Meta:
        abstract = True


class Student(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
