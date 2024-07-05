from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from urllib import request

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeated_password = request.POST['repeatPassword']
        
        if password == repeated_password:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                auth_login(request, user)
                return redirect('index')
            except:
                error_message = 'error creating account please try again'
                return redirect(request, 'signup.html', {'error_message': error_message})
        else:
            error_message = 'password is incorrect'
            return render(request, 'signup.html', {'error_message':error_message})
        
    return render(request, 'signup.html')
        
def logout(request):
    pass
def index(request):
    return render(request, 'index.html')