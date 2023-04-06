from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):
    dji=request.GET.get('myinput','dvalue')
    djcbox=request.GET.get('cbox','off')
    # print(djcbox)
    a=['0','1','2','3','4','5','6','7','8','9']
    an=""
    if djcbox=='on':
        for i in dji:
            if i not in a:
                an+=i
        dic={'string':an}
        return render(request,"page1.html",dic)
    else:
        dic={'string':dji}
        return render(request,"page1.html",dic)