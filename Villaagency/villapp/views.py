from django.shortcuts import render
from . models import signup
# Create your views here.


def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def pro(request):
    return render(request, 'properties.html')

def prodetails(request):
    return render(request, 'property_details.html')