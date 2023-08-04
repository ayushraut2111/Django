from rest_framework import serializers
from .models import student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    subject=serializers.CharField(max_length=50)

    def create(self, validated_data):
        return student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.subject=validated_data.get('subject',instance.subject)

        instance.save()
        return instance
    