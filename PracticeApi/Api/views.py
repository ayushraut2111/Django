from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

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
            
    def post(self,request,*args,**kwargs):
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