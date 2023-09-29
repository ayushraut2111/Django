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
    data=User1.objects.all()
    print(data[0].username)
    ser=UserSerializer(data,many=True)
    # print(list(ser.data[0]['id']))
    return Response(ser.data)

