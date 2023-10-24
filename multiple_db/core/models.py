from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)
    subject=models.CharField(max_length=255,blank=True,null=True)


class Book(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)


