# i have created this file 

from django.http import HttpResponse    # to import request and response use this
from django.shortcuts import render  # to work with templates

def index(request):     #any function take request and return response 
    return render(request,"index.html")   # using tamplate in our django  using render

def removepunc(request):
    return HttpResponse("remove punc <button><a href='/'>back</a></button>")  #adding back button in our page

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("remove new line")

def spaceremove(request):
    return HttpResponse("remove space")

def charcount(request):
    return HttpResponse("count char")