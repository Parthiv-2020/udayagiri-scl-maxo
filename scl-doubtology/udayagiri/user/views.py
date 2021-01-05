from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth import logout

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.warning(request, "You are logged in")
            return redirect('home')
        else:
            messages.warning(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'auth_templates/login.html')

def user_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name=first_name, last_name=last_name, username=username, email=email, password=password
                    )
                    user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login')
        messages.warning(request, 'Password do not match')
        return redirect('register')
        
    return render(request, 'auth_templates/register.html')

def user_profile(request):
    return render(request, 'user/profile.html')

def user_forgot_password(request):
    return render(request, 'auth_templates/forgot_password.html')

def user_logout(request):
    logout(request)
    return redirect('home')