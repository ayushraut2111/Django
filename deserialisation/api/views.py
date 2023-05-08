from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import json
from .serialisers import StudentSerialiser
import io
from django.views.decorators.csrf import csrf_exempt
def home(request):
    return HttpResponse("i am home")

@csrf_exempt
def stucreate(request):
    if request.method=='POST':
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        deserialiser=StudentSerialiser(data=python_data)
        if deserialiser.is_valid():
            deserialiser.save()
            res={'msg':'data created'}
            msg=json.dumps(res)
            return HttpResponse(msg)
    else:
        return HttpResponse("hello")


