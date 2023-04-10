from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import feature
def home(request):
    features=feature.objects.all()
    print(features)
    dic={'fr':features}
    return render(request,'index.html',dic)
 
def register(request):   #authentication form
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        details=request.POST.get("details")
        password=request.POST.get("password")
        password1=request.POST.get("password1")
        print(username,email,details,password,password1)
        if password==password1:
            if User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username matches')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request,'please enter the same password')
            return redirect('register')
    else:
        return render(request,'register.html')