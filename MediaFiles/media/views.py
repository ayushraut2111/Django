from django.shortcuts import render,redirect
from rest_framework.viewsets import ModelViewSet
from .models import picture
from .serializers import PicSerializer
from rest_framework.response import Response


def home(request):
    return render(request,'home.html')

class pic(ModelViewSet):
    queryset=picture.objects.all()
    serializer_class=PicSerializer

    def create(self, request):
        ser=PicSerializer(data=request.data,context={'request':request})
        print("ayush")
        if ser.is_valid():
            print("hello")
            ser.save()
            print("ayush")
            return redirect('/home')
        return Response({'msg':'created'})
    
    # def list(self, request, *args, **kwargs):
    #     pc=picture.objects.all()
    #     ser=PicSerializer(pc,many=True)
    #     return Response(ser.data)
    # def retrieve(self, request, pk,*args, **kwargs):
    #     pc=picture.objects.get(id=pk)
    #     ser=PicSerializer(pc)
    #     return Response(ser.data)
    
    # def destroy(self, request,pk):
    #     pc=picture.objects.get(id=pk)
    #     pc.delete()
    #     return Response({'msg':'deleted'})
    # def update(self, request,pk):
    #     pc=picture.objects.get(pk)
    #     ser=PicSerializer(pc,request.data)
    #     if ser.is_valid():
    #         ser.save()
    #     return Response({'msg':'updated'})