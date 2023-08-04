from django.db import models

class student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    subject=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
