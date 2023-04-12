from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
def index(request):
    return render(request,"index.html")

def register(reuqest):
    if reuqest.method=="POST":
        usr=reuqest.POST.get("username")
        eml=reuqest.POST.get("email")
        pwd1=reuqest.POST.get("password")
        pwd2=reuqest.POST.get("password1")
        print(usr,eml,pwd1,pwd2)
        if pwd1==pwd2:
            if User.objects.filter(email=eml).exists():
                messages.info(reuqest,"email alerady exist")
                return redirect('register')
            elif User.objects.filter(username=usr).exists():
                messages.info(reuqest,"username not available")
                return redirect('register')
            else:
                user=User.objects.create_user(username=usr,email=eml,password=pwd1)
                user.save()
                messages.info(reuqest,"user created")
                return redirect('login')
        else:
            messages.info(reuqest,"password unmatches")
            return redirect('register')
    else:    
        return render(reuqest,"register.html")

def login(request):
    if request.method=="POST":
        usr=request.POST.get("username")
        pwd=request.POST.get("password")
        user=auth.authenticate(username=usr,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"user not found")
            return redirect("login")
    else:    
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")
