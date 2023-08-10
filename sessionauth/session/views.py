from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import student
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,IsAdminUser
from .permissions import Mypermision

class student_api(ModelViewSet):
    queryset=student.objects.all()
    serializer_class=StudentSerializer

    authentication_classes=[SessionAuthentication]
    permission_classes=[Mypermision]