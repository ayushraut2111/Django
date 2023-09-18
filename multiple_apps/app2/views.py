from django.shortcuts import render,HttpResponse
import requests


def home(request):
    r=requests.get(url="http://127.0.0.1:8000/app1/people")
    print(r.json()['usr'][0])
    return HttpResponse("hello i am app2")
