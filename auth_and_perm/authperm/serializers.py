from rest_framework.serializers import ModelSerializer
from .models import student

class StudentSerializer(ModelSerializer):
    class Meta:
        model=student
        fields='__all__'
    