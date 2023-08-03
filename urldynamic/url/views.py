from django.shortcuts import render
from .serializers import StudentSerializer
from .models import student
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt
def home(request):
    #  serialization and changing model data into json data
    s1=student.objects.all()
    serial=StudentSerializer(s1,many=True)
    json_data=JSONRenderer().render(serial.data)
    print(json_data)
    return HttpResponse(json_data)

def single(request,pk):
    s1=student.objects.get(id=pk)
    serial=StudentSerializer(s1)
    json_data=JSONRenderer().render(serial.data)
    return HttpResponse(json_data)


def index(request,pk):
    # print(pk)
    return render(request,'index.html',{'pk':pk})

@csrf_exempt
def create_student(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        py_data=JSONParser().parse(stream)
        deserialser=StudentSerializer(data=py_data)
        if deserialser.is_valid():
            deserialser.save()
            return HttpResponse("saved")
        else:
            return HttpResponse("not valid")
