from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class StudentSerializer(ModelSerializer):
    naming=serializers.CharField(max_length=255,default="AYUSH",read_only=True)
    def create(self, validated_data):
        print(validated_data)
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        print(validated_data)
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.subject=validated_data.get('subject',instance.subject)
        instance.save()
        return instance
    class Meta:
        model=Student
        fields='__all__'