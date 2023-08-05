from rest_framework import serializers
from .models import student


def start_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError("name not start with r")
    
def end_with_a(value):
    if value[-1].lower()!='a':
        raise serializers.ValidationError("not ending with a")
   
    
class StudentSerializer(serializers.ModelSerializer):
    name=serializers.CharField(validators=[start_with_r,end_with_a])
    class Meta:
        model=student
        fields='__all__'     # fields=['name','roll','subject']

    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError("max value reached")
        return value
    def validate(self, data):
        name=data.get("name")
        roll=data.get("roll")
        if name=='ayush' and roll!=14:
            raise serializers.ValidationError("roll no. not matched")
        return data


# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=100,validators=[start_with_r,end_with_a])
#     roll=serializers.IntegerField()
#     subject=serializers.CharField(max_length=50)

#     def create(self, validated_data):
#         return student.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.roll=validated_data.get('roll',instance.roll)
#         instance.subject=validated_data.get('subject',instance.subject)

#         instance.save()
#         return instance
    
#     def validate_roll(self,value):
#         if value>=200:
#             raise serializers.ValidationError("max value reached")
#         return value
    
    # def validate(self, data):
    #     name=data.get("name")
    #     roll=data.get("roll")
    #     if name=='ayush' and roll!=14:
    #         raise serializers.ValidationError("roll no. not matched")
    #     return data
    