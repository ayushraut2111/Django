from django.http import HttpResponse
from django.shortcuts import render
from .models import Room
rooms=[{'id':1,'name':'Ayush'},
      {'id':2,'name':'Anish'},
      {'id':3,'name':'Sidhant'},
      {'id':4,'name':'Shivam'}]
def home(request):
    context={'rooms':rooms}
    return render(request,'base/index.html',context)

def room(request,pk):
    context=None
    for i in rooms:
        # print(i,pk)
        if i['id']==int(pk):
            context=i
            break
    print(context)
    return render(request,'base/room.html',context)
