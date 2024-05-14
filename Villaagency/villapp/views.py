from django.shortcuts import render, redirect
from . models import signup1, adminadd
from . forms import signforms
from django.contrib.auth import authenticate, login as auhtlogin, logout as authlogout
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
                    request.session['log']=username
                    return redirect('index')
                else:
                    return redirect('error')
        except signup1.DoesNotExist:
            print('error')
    return render(request,'login.html')

def profile(request):
    users=request.session['login.html']
    dataset=signup1.objects.get(username=users)
    return render(request,'profile.html' ,{'d':dataset})


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

def adminadd(request):
    if request.POST:
        totalflat=request.POST.get('totalflat')
        floorno=request.POST.get('floorno')
        numberofrooms=request.POST.get('numberofrooms')
        parking=request.POST.get('parking')
        payment=request.POST.get('payment')
        description=request.POST.get('description')
        objj=adminadd(total_flat_space=totalflat, floor_no=floorno, number_of_rooms=numberofrooms,parking_available=parking, payment_process=payment ,description=description)
        objj.save()
    return render(request, 'admin_add.html')

