from rest_framework.generics import ListAPIView,CreateAPIView
from .models import student
from .serializers import StudentSerializer
from .mypaginations import cursorpage

class studentlist(ListAPIView,CreateAPIView):
    queryset=student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=cursorpage