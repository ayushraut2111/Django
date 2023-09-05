from .models import CustomUser
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    password=serializers.CharField(write_only=True)
    password1=serializers.CharField(write_only=True)
    def create(self, validated_data):
        return CustomUser.objects.create_user(username=validated_data['username'],password=validated_data['password'],email=validated_data['email'],phone=validated_data['phone'])
    class Meta:
        model=CustomUser
        fields='__all__'
    def validate(self, attrs):
        print(attrs)
        password1=attrs.get('password')
        password2=attrs.get('password1')
        if password1!=password2:
            raise serializers.ValidationError("password not matched")
        return attrs
    def validate_email(self,value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("email exists")
        return value

    

