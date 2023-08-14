from .models import student
from rest_framework.serializers import ModelSerializer

class StudentSerializer(ModelSerializer):
    class Meta:
        model=student
        fields='__all__'