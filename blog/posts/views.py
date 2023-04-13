from django.shortcuts import render
from .models import Posts

def index(request):
    pst=Posts.objects.all()
    dic={'posts':pst}
    return render(request,"index.html",dic)