from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin

class CustomManager(BaseUserManager):
    def create_user(self,**kwargs):
        if not kwargs['phone']:
            raise ValueError("phone number is required")
        user=self.model(**kwargs)
        user.set_password(kwargs['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self,**kwargs):
        kwargs.setdefault('is_active',True)
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_superuser',True)
        user=self.create_user(**kwargs)
        return user

class CustomUser(AbstractBaseUser,PermissionsMixin):
    phone=models.IntegerField(unique=True)
    username=models.CharField(max_length=255)
    address=models.TextField()
    gender=models.CharField(max_length=20)
    is_staff=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)

    objects=CustomManager()
    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=[]

    def __str__(self) -> str:
        return self.username