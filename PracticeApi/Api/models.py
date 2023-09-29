from django.db import models

class Student(models.Model):
    roll=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255,blank=True,null=True)
    subject=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self) -> str:
        return self.name
