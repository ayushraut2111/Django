from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import student
from .customauth import CustomAuth
from rest_framework.permissions import IsAuthenticated

class student_api(ModelViewSet):
    queryset=student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[CustomAuth]    
    permission_classes=[IsAuthenticated]
