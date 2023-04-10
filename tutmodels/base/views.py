from django.shortcuts import render
from .models import feature
def home(request):
    features=feature.objects.all()
    print(features)
    dic={'fr':features}
    return render(request,'index.html',dic)
 
def register(request):
    username=request.POST.get("username")
    email=request.POST.get("email")
    details=request.POST.get("details")
    password=request.POST.get("password")
    password1=request.POST.get("password1")
    print(username,email,details,password,password1)
    if password==password1:
        pass
    return render(request,'register.html')