# i have created this file 

from django.http import HttpResponse

def index(request):     #any function take request and return response 
    return HttpResponse("hello")

def about(request):
    return HttpResponse("<h1>Hello</h1>")