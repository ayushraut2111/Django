from django.db import models
from datetime import datetime

class Posts(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=1000000000)
    created_at=models.DateTimeField(default=datetime.now(),blank=True)
