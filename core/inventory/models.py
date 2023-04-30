from django.db import models

class Product(models.Model):
    name=models.CharField("fruit name",max_length=1000)
    qty=models.IntegerField()
    colour=models.CharField(max_length=100,choices=[('red','red'),('green','green'),('blue','blue')],default="blackwhite")

    def __str__(self) -> str:
        return self.name

class Brand(models.Model):
    name=models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
# class course(models.Model):
#     course_id=models.CharField(max_length=100,primary_key=True)
#     course_name=models.CharField(max_length=100)

#     def __str__(self):
#         return self.course_name
    

# class student(models.Model):
#     roll_number=models.IntegerField(primary_key=True)
#     name=models.CharField(max_length=100)
#     course=models.ForeignKey(course,on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name

# class Room(models.Model):
#     room_no=models.IntegerField(primary_key=True)
#     room_name=models.CharField(max_length=100)
#     student=models.OneToOneField(student,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.room_no
# class studentONE(models.Model):
#     roll_number=models.IntegerField(primary_key=True)
#     name=models.CharField(max_length=100)
#     course=models.ForeignKey(course,on_delete=models.CASCADE)
#     room=models.OneToOneField(Room,on_delete=models.CASCADE)

    

