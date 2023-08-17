from django.shortcuts import render,redirect
from rest_framework.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

class signup(View):
    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"email exists please go to login page")
                redirect('/signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"username exists please enter different username")
                redirect('/signup')
            else:
                usr=User.objects.create_user(username=username,email=email,password=password1)
                usr.save()
                return redirect('/login') 
        else:
            messages.info(request,"password not matched")
            redirect('/signup')
        return render(request,'signup.html')



class login(View):
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        username=request.POST['username']
        pwd=request.POST['password']
        usr=auth.authenticate(username=username,password=pwd)

        if usr is not None:
            auth.login(request,usr)
            messages.info(request,"user logged in")
            return redirect('/login')
        else:
            messages.info(request,"enter valid credentials")
            return redirect('/login')
        

class logout(View):
    def get(self,request):
        auth.logout(request)
        redirect('/login')
        return render(request,'login.html')
    
class student_api(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    # filter_backends=[OrderingFilter]    these filters are only used when we havent used any view filters in methods
    # search_fields=['name','subject']
    
    def create(delf,request):
        print(request.data.get('roll'))
        stu=StudentSerializer(data=request.data)
        if stu.is_valid():
            stu.save()
            s=Student.objects.get(roll=request.data.get('roll'))
            s.user=request.user
            s.save()
            return Response({'msg':'created'})
        
    def list(self, request, *args, **kwargs):
        stu=Student.objects.filter(user=request.user)
        serialiser=StudentSerializer(stu,many=True)
        return Response(serialiser.data,status=status.HTTP_202_ACCEPTED)