from django.shortcuts import render,HttpResponse


def home(request):
    return HttpResponse("hello i am app1")
