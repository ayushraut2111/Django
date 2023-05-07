from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serialisers import StudentSerialiser
from rest_framework.renderers import JSONRenderer

def home(request):
    return HttpResponse("hello i am home")

def student_details(request):
    stu=Student.objects.all()
    serialise=StudentSerialiser(stu,many=True)
    # json_data=JSONRenderer().render(serialise.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serialise.data,safe=False)
