from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import student
from .serializers import StudentSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return HttpResponse("hello")

@csrf_exempt
def student_api(request):
    if request.method=='GET':
        data=request.body
        stream=io.BytesIO(data)
        py_data=JSONParser().parse(stream)
        id=py_data.get('id',None)
        if id is not None:
            stu=student.objects.get(id=id)
            serialise=StudentSerializer(stu)
            json_data=JSONRenderer().render(serialise.data)
            return HttpResponse(json_data)
        
        stu=student.objects.all()
        serialise=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serialise.data)
        return HttpResponse(json_data)
    
    if request.method=='POST':
        data=request.body
        stream=io.BytesIO(data)
        py_data=JSONParser().parse(stream)
        serialise=StudentSerializer(data=py_data)
        if serialise.is_valid():
            serialise.save()
            return HttpResponse("hello")
        else:
            json_data=json.dumps(serialise.errors)
            return HttpResponse(json_data)
    
    if request.method=='PUT':
        data=request.body
        stream=io.BytesIO(data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id')
        stu=student.objects.get(id=id)
        serialise=StudentSerializer(stu,data=pydata,partial=True)
        if serialise.is_valid():
            serialise.save()

    if request.method=='DELETE':
        data=request.body
        stream=io.BytesIO(data)
        py_data=JSONParser().parse(stream)
        id=py_data.get('id')
        s1=student.objects.get(id=id)
        s1.delete()
        msg={'msg':'data deleted'}
        msg=json.dumps(msg)
        return HttpResponse(msg)

