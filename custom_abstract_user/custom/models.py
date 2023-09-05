from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


class CustomManager(BaseUserManager):
    def create_user(self,**kwargs):
        if not kwargs['phone']:                                   # phone no. is required
            raise ValueError("phone number is required")
        print(kwargs)
        kwargs['email']=self.normalize_email(kwargs['email'])   # we have to normalize email as cap letter and small letter are same
        user=self.model(**kwargs)    # getting all values in model
        user.set_password(kwargs['password'])
        user.save(using=self.db)
        return user

    def create_superuser(self,**kwargs):
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_superuser',True)
        kwargs.setdefault('is_active',True)
        user=self.create_user(**kwargs)    # creating user normally then giving it extra permissions
        return user

class CustomUser(AbstractUser):
    phone=models.CharField(max_length=15,unique=True)
    email=models.EmailField(unique=True)
    bio=models.TextField()

    objects=CustomManager()

    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=['email']

