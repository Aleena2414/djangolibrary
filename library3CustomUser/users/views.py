from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from users.models import users

from users.models import CustomUser


# Create your views here.
def adminregister(request):
    if(request.method=='POST'):
        u=request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        a=request.POST['a']
        ph=request.POST['ph']

        if(p==cp):
            u=CustomUser.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e,address=a,phone=ph,is_superuser=True)
            u.save()
        else:
            return HttpResponse("password is not matching")
        return redirect('users:login')
    return render(request,'adminregister.html')

def userregister(request):
    if(request.method=='POST'):
        u=request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        a=request.POST['a']
        ph=request.POST['ph']

        if(p==cp):
            u=CustomUser.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e,address=a,phone=ph,is_user=True)
            u.save()
        else:
            return HttpResponse("password is not matching")
        return redirect('users:login')
    return render(request,'userregister.html')
def userlogin(request):
    if(request.method=='POST'):
        u = request.POST['u']
        p = request.POST['p']

        user=authenticate(username=u, password=p)
        if user and user.is_superuser==True:
            login(request,user)
            return redirect('books:home')
        elif user and user.is_user == True:
            login(request, user)
            return redirect('books:home')
        else:
            return HttpResponse('invalid')

    return render(request,'login.html')
def viewuser(request):
    k=users.objects.all()
    context={'users':k}
    return render(request,'viewuser.html',context)


def userlogout(request):
    logout(request)
    return redirect('users:login')
