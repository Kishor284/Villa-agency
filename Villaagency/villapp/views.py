from django.shortcuts import render, redirect, reverse
from . models import signup1, sdata,  villaimage, Data
from . models import Data as Data1
from . forms import signforms, Leaveform, villaimageform, Dataform
from django.contrib.auth import authenticate, login as auhtlogin, logout as authlogout
from django.conf import settings
from django.http import HttpResponse
import os
from urllib.parse import quote
# Create your views here.


def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.POST:
        name=request.POST.get('name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        phoneno=request.POST.get('numbers')
        gmail=request.POST.get('gmail')
        obj=signup1(name=name, username=username, password=password, phoneno=phoneno, gmail=gmail)
        obj.save()
    return render(request,'signup.html')

def login(request):
    if request.POST:
        username=request.POST.get('name')
        password=request.POST.get('password')
        try:
            user1=signup1.objects.get(username=username)
            if user1.username==username:
                if password==user1.password:
                    request.session['login']=username
                    return redirect('home')
                else:
                    return redirect('error')
        except signup1.DoesNotExist:
            print('error')
    return render(request,'login.html')

def profile(request):
    users=request.session['login']
    dataset=signup1.objects.get(username=users)
    if request.POST:
        phoneno=request.POST.get('phoneno')
        email=request.POST.get('gmail')
        dataset.phoneno=phoneno
        dataset.gmail=email
        dataset.save()
    else:
        return render(request,'profile.html' ,{'d':dataset})
    return render(request, 'profile.html',{'d':dataset})
    

def home(request):
    return render(request, 'home.html')

def pro(request):
    return render(request, 'properties.html')

def contact(request):
    return render(request, 'contact.html')


def prodetails(request):
    return render(request, 'property_details.html')

def error(request):
    return render(request, 'error.html')

def admin(request):
    return render(request, 'admin.html')

def users(request):
    datas=signup1.objects.all()
    return render(request, 'users.html',{'userss':datas})

def details_delete(request):
    datas=signup1.objects.all()
    return render(request, 'user_details.html', {'userss':datas})

def delete1(request,pk):
    instance=signup1.objects.get(pk=pk)
    instance.delete()
    datas=signup1.objects.all()
    return render(request, 'user_details.html', {'userss':datas})


def sdataform(request):
    if request.POST:
        form = Leaveform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(admin) 
    return render(request,'admin_data_add.html')


def success(request):
    return HttpResponse('successfully uploaded')

def admin_views_datas(request):
    views=sdata.objects.all()
    return render(request, 'admin_data_view.html',{'userss':views})

def uploads(request):
    print('hi')
    if request.POST:
        form=villaimageform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form=villaimageform()
    return render(request, 'imgupload.html',{'form':form})


def Data(request):
    if request.POST:
        form = Dataform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success') 
    else:
        form=Dataform()
    return render(request,'Dataadd.html',{'form': form})


def cart(request):
    return render(request, 'cart.html',)

def dataviewss(request):
    dviews=Data1.objects.all()
    return render(request, 'dataview.html',{'userss':dviews})



