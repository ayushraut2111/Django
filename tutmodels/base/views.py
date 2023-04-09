from django.shortcuts import render
from .models import feature
def home(request):
    
    return render(request,'index.html')
