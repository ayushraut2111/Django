from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def register(reuqest):
    if reuqest.method=="POST":
        pass
    else:    
        return render(reuqest,"register.html")

def login(request):
    pass

def logout(request):
    pass
