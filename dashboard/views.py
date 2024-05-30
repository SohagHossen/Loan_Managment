from django.http import HttpResponse
from django.shortcuts import render
from dashboard.models import Desh_inf
# Create your views here.


def dashboard(request):
    return render(request,"dashboard.html")



def desh_info(request):
    deshinfo = Desh_inf.objects.all()
    return render(request, 'dashboard.html', {'deshinfo':deshinfo})