from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student
from . serializers import StudentSerialiser
from rest_framework import status

@api_view(['GET','POST'])
def home(request):
    if request.method=='POST' or request.method=='GET':
        return Response({'msg':'i am home'})

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def api_show(request,pk=None):
    if request.method=='GET':
        if pk is not None:
            stu=student.objects.get(id=pk)
            serializer=StudentSerialiser(stu)
            return Response(serializer.data,status=status.HTTP_302_FOUND)
        stu=student.objects.all()
        serializer=StudentSerialiser(stu,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=StudentSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data saved'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='PATCH':
        id=pk
        st=student.objects.get(id=id)
        serializer=StudentSerialiser(st,request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated successfully'},status=status.HTTP_202_ACCEPTED)
        return Response({'msg':"ot updated"},status=status.HTTP_304_NOT_MODIFIED)
    
    if request.method=='PUT':
        id=pk
        st=student.objects.get(id=id)
        serializer=StudentSerialiser(st,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated successfully'},status=status.HTTP_202_ACCEPTED)
        return Response({'msg':"ot updated"},status=status.HTTP_304_NOT_MODIFIED)
    
    if request.method=='DELETE':
        id=pk
        stu=student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'data deleted'},status=status.HTTP_410_GONE)
    
    

    # this pk will work on browser api 
    # for working with myapp.py we have to extract the data sent by myapp.py as ===> id=request.data.get('id)