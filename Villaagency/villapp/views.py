from django.shortcuts import render, redirect
from . models import signup
from . forms import signforms
from django.contrib.auth import authenticate, login as auhtlogin, logout as authlogout
# Create your views here.


def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.post:
        frm=signforms(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm=signforms()
    return render(request,'signup.html')

def login(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user1=signup.objects.get(username=username)
            if user1.username==username:
                if password==user1.password:
                    request.session['log']=username
                    return redirect('')
                
        except signup.DoesNotExist:
            print('error')
    return render(request,'login.html')

def profile(request):
    users=request.session['login.html']
    dataset=signup.objects.get(username=users)
    return render(request,'profile.html' ,{'d':dataset})


def pro(request):
    return render(request, 'properties.html')

def prodetails(request):
    return render(request, 'property_details.html')