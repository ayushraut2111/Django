from rest_framework import serializers
from .models import student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    subject=serializers.CharField(max_length=50)

    def create(self, validated_data):
        return student.objects.create(**validated_data)