# i have created this file 

from django.http import HttpResponse    # to import request and response use this

def index(request):     #any function take request and return response 
    return HttpResponse("hello this is homepage")

def about(request):
    return HttpResponse("<h1>Hello i am about</h1>")