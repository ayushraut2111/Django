# i have created this file 

from django.http import HttpResponse    # to import request and response use this

def index(request):     #any function take request and return response 
    return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("remove new line")

def spaceremove(request):
    return HttpResponse("remove space")

def charcount(request):
    return HttpResponse("count char")