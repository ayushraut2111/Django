from django.db import models


class User1(models.Model):
    username=models.CharField(max_length=50,null=True,unique=True)

    def __str__(self) -> str:
        return self.username
    
class People(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    user=models.ForeignKey(User1,on_delete=models.CASCADE,related_name="usr")

    def __str__(self) -> str:
        return self.name
