from django.shortcuts import render
from rest_framework.views import View
from rest_framework.viewsets import ModelViewSet
from .models import student
from .serializers import StudentSerializer
class home(View):
    def get(self,request):
        return render(request,'index.html')
    

class studentapi(ModelViewSet):
    queryset=student.objects.all()
    serializer_class=StudentSerializer

