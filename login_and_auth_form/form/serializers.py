from rest_framework.serializers import ModelSerializer
from .models import Student
from django.contrib.auth.models import User


class StudentSerializer(ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
    def create(self,validated_data):
        stu=Student.objects.create(**validated_data)
        return stu
    