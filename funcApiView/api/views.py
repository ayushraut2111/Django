from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerialiser
from . models import student

class home(APIView):
    def get(self,request,pk=None):
        return Response({'msg':"hello i am home"})
    
class api_show(APIView):
    def get(self,request,pk=None,format=None):
        if pk is not None and student.objects.filter(id=pk).exists():
            stu=student.objects.get(id=pk)
            serializer=StudentSerialiser(stu)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif not student.objects.filter(id=pk).exists():
            return Response({'msg':"data does not exist"},status=status.HTTP_400_BAD_REQUEST)
        stu=student.objects.all()
        serializer=StudentSerialiser(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=StudentSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"data saved"},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk=None):
        if not student.objects.filter(id=pk).exists():
            return Response({'msg':"data does not exist"},status=status.HTTP_400_BAD_REQUEST)
        stu=student.objects.get(id=pk)
        serializer=StudentSerialiser(stu,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"data updated"},status=status.HTTP_202_ACCEPTED)
        
    def patch(self,request,pk=None):
        if not student.objects.filter(id=pk).exists():
            return Response({'msg':"data does not exist"},status=status.HTTP_400_BAD_REQUEST)
        stu=student.objects.get(id=pk)
        serializer=StudentSerialiser(stu,request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"data updated"},status=status.HTTP_202_ACCEPTED)
    
    def delete(self,request,pk):
         if not student.objects.filter(id=pk).exists():
            return Response({'msg':"data does not exist"},status=status.HTTP_400_BAD_REQUEST)
         s1=student.objects.get(id=pk)
         s1.delete()
         return Response({"msg":"data deleted"},status=status.HTTP_410_GONE)
    
