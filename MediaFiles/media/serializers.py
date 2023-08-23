from .models import picture
from rest_framework.serializers import ModelSerializer

class PicSerializer(ModelSerializer):
    def create(self, validated_data):
        validated_data['image']=self.context['request'].FILES['image']
        print(validated_data)
        return picture.objects.create(**validated_data)

    class Meta:
        model=picture
        fields='__all__'
