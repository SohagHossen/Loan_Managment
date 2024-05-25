from django.shortcuts import render
from django.http import HttpResponse
def customer(request):
    return  HttpResponse("Hello, world. You're at the customer view.")

# Create your views here.
