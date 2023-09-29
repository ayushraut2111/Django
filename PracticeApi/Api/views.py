from rest_framework.views import APIView,View
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.contrib.auth.models import User,auth
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class Signup(APIView):
    def post(self,request):
        username=request.data['username']
        email=request.data['email']
        pass1=request.data['pass1']
        pass2=request.data['pass2']
        # print(username,email,pass1,pass2)
        if pass1==pass2:
            if not User.objects.filter(email=email).exists():
                if not User.objects.filter(username=username).exists():
                    user=User.objects.create_user(username=username,email=email,password=pass1)
                    user.save()
                    return Response({"message":"user created"})
                else:
                    return Response({"message":"user with this username already exists"})
            else:
                return Response({"message":"email already registered"})
        else:
            return Response({"message":"password not matched"})



class ShowApi(APIView):
    def get(self,request,pk=None):
        if pk==None:
            try:
                obj=Student.objects.all()
                ser=StudentSerializer(obj,many=True)
                return Response(ser.data)
            except Exception as e:
                return Response({"message":str(e)})
        else:
            try:
                obj=Student.objects.get(pk=pk)
                ser=StudentSerializer(obj)
                return Response(ser.data)
            except Exception as e:
                return Response({"message":str(e)})
            
    def post(self,request,format=None):
        try:
            ser=StudentSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            else:
                return Response({"message":ser.errors})
        except Exception as e:
            return Response({"message":str(e)})
    
    def put(self,request,pk):
        try:
            instance=Student.objects.get(pk=pk)
            ser=StudentSerializer(instance,data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            else:
                return Response({"message":ser.errors})
        except Exception as e:
            return Response({"message":str(e)})
    def patch(self,request,pk):
        try:
            instance=Student.objects.get(pk=pk)
            print(instance, "partial update")
            ser=StudentSerializer(instance,data=request.data,partial=True)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            else:
                return Response({"message":ser.errors})
        except Exception as e:
            return Response({"message":str(e)})
        
    def delete(self,request,pk):
        try:
            obj=Student.objects.get(pk=pk)
            obj.delete()
            return Response({"message":"student removed"})
        except Exception as e:
            return Response({"message":str(e)})