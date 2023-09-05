from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager



class CustomManager(BaseUserManager):
    def create_user(self,**kwargs):
        if not kwargs['username']:
            raise ValueError("username not provided")
        user=self.model(**kwargs)
        user.set_password(kwargs['password'])
        user.save(using=self.db)
        return user


    def create_superuser(self,**kwargs):
        # print(kwargs)
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_active',True)
        kwargs.setdefault('is_superuser',True)
        user=self.create_user(**kwargs)
        return user

class CustomUser(AbstractBaseUser):
    username=models.CharField(max_length=50,unique=True)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    address=models.TextField() 
    is_staff=models.BooleanField(default=False)   # these fields are must
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    objects=CustomManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
