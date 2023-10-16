from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class StudentView(APIView):
    def get(self,request,pk=None):
        if pk is None:
            queryset=Student.objects.all()
            serializer=StudentSerializer(queryset,many=True)
            return Response(serializer.data)
        else:
            queryset=Student.objects.get(pk=pk)
            serializer=StudentSerializer(queryset)
            return Response(serializer.data)
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)