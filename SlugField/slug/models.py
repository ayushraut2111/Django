from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    class Meta:
        abstract = True


class Student(BaseModel):
    name=models.CharField(max_length=255,blank=True,null=True)
    roll=models.IntegerField()
    subject=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self) -> str:
        return self.name
    
