from django.db import models

class StudentManager(models.Manager):
    def between(self):
        return self.get_queryset().filter(roll__gt=2,roll__lt=4)


class Student(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)
    subject=models.CharField(max_length=255,blank=True,null=True)
    roll=models.IntegerField(blank=True,null=True)

    def __str__(self) -> str:
        return self.name
    
    objects=StudentManager()
