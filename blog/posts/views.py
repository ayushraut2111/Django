from django.shortcuts import render
from .models import Posts

def index(request):
    pst=Posts.objects.all()
    dic={'posts':pst}
    return render(request,"index.html",dic)

def post(request,pk):
    pst=Posts.objects.get(id=pk)
    return render(request,'post.html',{'post':pst})