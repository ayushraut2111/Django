from rest_framework import serializers
from . models import student

class StudentSerialiser(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'

        