from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import StudentSerializers
from .models import student
class api_view(ListCreateAPIView):
    queryset=student.objects.all()
    serializer_class=StudentSerializers

class api_view_pk(RetrieveUpdateDestroyAPIView):
    queryset=student.objects.all()
    serializer_class=StudentSerializers

