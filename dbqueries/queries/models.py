from django.db import models

class Course(models.Model):
    c_id=models.IntegerField(primary_key=True)
    c_name=models.CharField(max_length=100)

    def __str__(self):
        return self.c_name
    
class Room(models.Model):
    r_id=models.IntegerField(primary_key=True)
    r_name=models.CharField(max_length=100)

    def __str__(self):
        return self.r_name
    
class Student(models.Model):
    roll_no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    room=models.OneToOneField(Room,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

