from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout


def login(request):
    if request.method=='POST':
       username = request.POST.get('username')
       password = request.POST.get('password')

       user=auth.authenticate(username=username, password=password)
        
       if user is not None:
           auth.login(request,user) 
           return redirect("/")
       else:
            return HttpResponse('invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('Username taken')
                return HttpResponse('Username already taken')
            elif User.objects.filter(email=email).exists():
                print('Email taken')
                return HttpResponse('Email already taken')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                print('User created')
                return redirect('login')
        else:
            print('Passwords do not match')
            return HttpResponse('Passwords do not match')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
  
def index(request):
    return redirect('index')


