from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import mysql.connector

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def tut1(request):
    return render (request,'tutorial1.html')

def tut2(request):
    return render (request,'tutorial2.html')

def tut3(request):
    return render (request,'tutorial3.html')

def tut4(request):
    return render (request,'TUTORIAL4.html')

def nextt1(request):
    return render (request,'home.html')

def progress(request):
    return render (request,'progress.html')


def quiz(request):
    md= mysql.connector.connect(host='localhost',user='root',passwd='vibha',database='school',autocommit=True)
    c=md.cursor()
    c.execute(f"select q from question where sno =1")
    x=c.fetchone()
    c.execute(f"select q from question where sno =2")
    x1=c.fetchone()
    c.execute(f"select q from question where sno =3")
    x2=c.fetchone()
    c.execute(f"select q from question where sno =4")
    x3=c.fetchone()
    return render (request,'quiz.html',{'a':x[0],'b':x1[0],'c':x2[0],'d':x3[0]})



