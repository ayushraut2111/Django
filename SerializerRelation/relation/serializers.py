from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Song,Singer

class SongSerializer(ModelSerializer):
    class Meta:
        model=Song
        fields=['id','title','singer','duration']


class SingerSerializer(ModelSerializer):
    # song=serializers.StringRelatedField(many=True)
    song=serializers.HyperlinkedRelatedField(view_name='song-detail',many=True,read_only=True)
    class Meta:
        model=Singer
        fields=['id','name','gender','song']