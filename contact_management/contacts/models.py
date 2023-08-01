from django.db import models

class contacts(models.Model):
    name=models.CharField(max_length=255)
    number=models.IntegerField()

    def __str__(self) -> str:
        return self.name
