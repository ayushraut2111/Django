from django.http import HttpResponse    # to import request and response use this
from django.shortcuts import render  # to work with templates

def index(request):     #any function take request and return response 
    return render(request,"index.html")   # taking third argument as dictionary and using it in our html file

def analyze(request):
    djinp=request.GET.get('csk','ayush')
    # print(djinp)
    num=['0','1','2','3','4','5','6','7','8','9']
    an=""
    for i in djinp:
        if i not in num:
            an+=i
    duc={'rmp':'after removing number text is','atext':an}
    return render(request,"analyze.html",duc)