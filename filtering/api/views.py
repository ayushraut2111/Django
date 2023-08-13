from .models import student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet


class studentlist(ModelViewSet):
    queryset=student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['subject','passby']

    # def get_queryset(self):
    #     return student.objects.filter(passby=self.request.user)