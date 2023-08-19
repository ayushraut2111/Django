from rest_framework.serializers import ModelSerializer
from .models import details
class DetailSerializer(ModelSerializer):
    class Meta:
        model=details
        fields='__all__'

    def to_internal_value(self, data):
        if data.get('end_year') == '':
            data['end_year'] = None
        if data.get('intensity') == '':
            data['intensity'] = None
        if data.get('start_year') == '':
            data['start_year'] = None
        if data.get('relevance') == '':
            data['relevance'] = None
        if data.get('likelihood') == '':
            data['likelihood'] = None

        return super(DetailSerializer, self).to_internal_value(data)