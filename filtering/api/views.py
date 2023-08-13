from rest_framework.generics import ListAPIView,CreateAPIView
from .models import student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend


class studentlist(ListAPIView,CreateAPIView):
    queryset=student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['subject']

    # def get_queryset(self):
    #     return student.objects.filter(passby=self.request.user)