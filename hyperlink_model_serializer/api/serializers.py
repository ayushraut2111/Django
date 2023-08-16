from .models import student
from rest_framework.serializers import HyperlinkedModelSerializer

class StudentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model=student
        fields=['id','url','name','subject','roll']