from django.shortcuts import render,redirect
from rest_framework.views import View,APIView
from .models import CustomUser
from .serializers import UserSerializer

class home(View):
    def get(self,request):
        return render(request,'home.html')
    
class MakeUser(APIView):
    def post(self,request):
        print(request.data)
        ser=UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return redirect('/home')
        
    

# class MakeUser(APIView):  #without serializer
#     def post(self,request):
#         print(request.data)
#         usr=CustomUser.objects.create_superuser(username=request.data.get('username'),password=request.data.get('password'),email=request.data.get('email'),phone=request.data.get('phone'))
#         usr.save()
#         return redirect('/home')
