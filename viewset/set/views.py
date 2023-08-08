from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerialiser
from.models import student

class make_api(ViewSet):
    def list(self,request):
        stu=student.objects.all()
        serializers=StudentSerialiser(stu,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer=StudentSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        if student.objects.filter(id=pk).exists():
            stu=student.objects.get(id=pk)
            serializer=StudentSerialiser(stu)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'msg':"not a valid request"},status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        stu=student.objects.get(id=pk)
        serializer=StudentSerialiser(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        stu=student.objects.get(id=pk)
        serializer=StudentSerialiser(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        s1=student.objects.get(id=pk)
        s1.delete()
        return Response({'msg':"data deleted"},status=status.HTTP_410_GONE)
