from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse("hello")

def index(request):
    return render(request,"index.html")
