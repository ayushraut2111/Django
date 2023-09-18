from .models import User1,People
from rest_framework.serializers import ModelSerializer

class PeopleSerializer(ModelSerializer):
    class Meta:
        model=People
        fields='__all__'

class UserSerializer(ModelSerializer):
    usr=PeopleSerializer(many=True,read_only=True)
    class Meta:
        model=User1
        fields='__all__'