from rest_framework.viewsets import ModelViewSet
from .models import student
from .serializers import StudentSerializer

class studentlist(ModelViewSet):
    queryset=student.objects.all()
    serializer_class=StudentSerializer