from django.shortcuts import render
from . models import contacts
def home(request):
    if request.method=='POST':
        name=request.POST.get("save","no name")
        number=request.POST.get("number","0000000")
        contacts.objects.create(name=name,number=number)
        # contacts.objects.filter(name="anish").delete()
        c1=contacts.objects.filter(name="anish")
        c1.delete()
        c=contacts.objects.all()
        return render(request,"index.html",{'c':c})
    else:
        return render(request,"index.html")

def new(request):
    text=request.POST.get('save','default')
    c1=contacts.objects.get(id=3)
    print(c1)
    return render(request,"index.html",{'contact':c1})

def room(request,pk):
    return render(request,"index.html",{'name':pk})
