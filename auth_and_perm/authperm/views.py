from rest_framework.viewsets import ModelViewSet
from .models import student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions


class api_show(ModelViewSet):
    queryset=student.objects.all()
    serializer_class=StudentSerializer

    authentication_classes=[BasicAuthentication]
    permission_classes=[DjangoModelPermissions]