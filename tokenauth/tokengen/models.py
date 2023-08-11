from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


#this code created token with the help of signals

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)

class student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    subject=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
