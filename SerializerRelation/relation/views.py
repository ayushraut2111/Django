from rest_framework.viewsets import ModelViewSet
from .models import Song,Singer
from .serializers import SongSerializer,SingerSerializer

class singerviewset(ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer

class SongViewset(ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer
