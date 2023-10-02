from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class Signup(APIView):
    def post(self,request):
        try:
            # print(request.data)
            if CustomUser.objects.filter(phone=request.data['phone']).exists():
                return Response({"message":"phone number already exists"})
            serializer=UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"user created"})
            else:
                return Response({serializer.error_messages})
        except Exception as e:
            return Response({"message":str(e)})
