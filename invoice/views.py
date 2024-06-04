from django.shortcuts import render
from django.views import View

# Create your views here.


def invoice(request):

     return render(request , 'invoice.html')

class class_data(View):
     def get(self,request):
          return render(request,'class_data.html')
