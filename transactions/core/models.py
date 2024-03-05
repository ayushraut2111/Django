from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
