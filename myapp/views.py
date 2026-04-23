from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# Create your views here.

def apple(request):
    return render(request,'apple.html')

def appledata(request):
    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpass=request.POST.get('cpass')
        phone=request.POST.get('phone')

        #insertquery
        insertquery=AppleModel(fname=fname,lname=lname,email=email,password=password,cpass=cpass,phone=phone)
        insertquery.save()
        messages.success(request,'Registration Successful')
        return render(request,'apple.html')

def login(request):
    return render(request,'login.html')

def logindata(request):
    if request.method == 'POST':
        uemail=request.POST.get('uemail')
        upassword=request.POST.get('upassword')

        print (uemail,upassword)

        try:
            userdata = AppleModel.objects.get(email=uemail,password=upassword)
            #SESSION
            request.session['log_id']=userdata.id
            request.session['user_email']=userdata.email
            request.session['user_password']=userdata.password

            request.session.save()

            print("session started successfully")
            print("login successfully")

            messages.success(request,'Login Successful')
            return redirect('/apple')
        except:
            userdata=None
            print("login failed")
            messages.error(request,'Invalid credentials')
            return redirect('/login')

        if userdata is None:
            print("login Successfully")

        return render(request,'login.html')
