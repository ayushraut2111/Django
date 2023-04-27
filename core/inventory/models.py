from django.db import models

class Product(models.Model):
    name=models.CharField("fruit name",max_length=1000)
    qty=models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Brand(models.Model):
    name=models.CharField(max_length=1000)

    def __str__(self):
        return self.name
