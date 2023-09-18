from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from .models import User1
from .serializers import UserSerializer
from rest_framework.response import Response
import requests


def home(request):
    return HttpResponse("hello i am app1")

@api_view(['GET'])
def apiview(request):
    print("helllo")
    data=User1.objects.get(id=1)
    ser=UserSerializer(data)
    print(ser)
    return Response(ser.data)

