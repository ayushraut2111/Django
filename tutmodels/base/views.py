from django.shortcuts import render
from .models import feature
def home(request):
    features=feature.objects.all()
    print(features)
    dic={'fr':features}
    return render(request,'index.html',dic)
 