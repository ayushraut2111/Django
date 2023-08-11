from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import student
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class student_api(ModelViewSet):
    queryset=student.objects.all()
    serializer_class=StudentSerializer

    authentication_classes=[TokenAuthentication]    
    permission_classes=[IsAuthenticated]


# http http://127.0.0.1:8000/student/ 'Authorization:Token 5b49d0efa83234fc43971dd4fb9667093542f6a6'
# http GET http://127.0.0.1:8000/student/ 'Authorization:Token 5b49d0efa83234fc43971dd4fb9667093542f6a6'  same as above
# http DELETE http://127.0.0.1:8000/student/1/ 'Authorization:Token 5b49d0efa83234fc43971dd4fb9667093542f6a6'