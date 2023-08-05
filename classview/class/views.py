from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View

class home(TemplateView):
    template_name='home.html'

# class home(View):
#     def get(self,request):
#         return render(request,'home.html')
    