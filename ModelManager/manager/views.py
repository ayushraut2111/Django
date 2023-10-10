from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from .pagination import CustomPagination

class StudentView(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=CustomPagination

    def get_queryset(self):
        queryset=Student.objects.between()
        return queryset
