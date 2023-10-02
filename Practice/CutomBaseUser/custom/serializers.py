from .models import *
from rest_framework import serializers
from .models import CustomUser
from rest_framework.serializers import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    pass2=serializers.CharField(write_only=True)
    def create(self, validated_data):
        print("ayush")
        print(validated_data)
        return CustomUser.objects.create_user(phone=validated_data['phone'],username=validated_data['username'],address=validated_data['address'],gender=validated_data['gender'],password=validated_data['password'])
    class Meta:
        model=CustomUser
        fields='__all__'

    def validate(self, attrs):
        print(attrs)
        if attrs.get('password')!=attrs.get('pass2'):
            raise ValueError("password not matched")
        return attrs
    def validate_phone(self,value):
        print(value)
        if CustomUser.objects.filter(phone=value).exists():
            raise ValidationError("phone number already registered")
        return value