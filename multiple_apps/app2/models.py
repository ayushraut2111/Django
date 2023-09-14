from django.db import models


class User2(models.Model):
    username=models.CharField(max_length=50,null=True,unique=True)

    def __str__(self) -> str:
        return self.username
