from django.shortcuts import render

def user_login(request):
    return render(request, 'auth_templates/login.html')

def user_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        print(first_name, last_name)
    return render(request, 'auth_templates/register.html')

def user_profile(request):
    return render(request, 'user/profile.html')

def user_forgot_password(request):
    return render(request, 'auth_templates/forgot_password.html')


# def register(request):
#     if request.method == 'POST':
#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']

#         if password == confirm_password:
#             if User.objects.filter(username=username).exists():
#                 messages.warning(request, 'Username exists')
#                 return redirect('register')
#             else:
#                 if User.objects.filter(email=email).exists():
#                     messages.warning(request, 'email already exists')
#                     return redirect('register')
#                 else:
#                     user = User.objects.create_user(
#                         first_name=firstname, last_name=lastname, username=username, email=email, password=password)
#                     user.save()
#                     messages.success(request, 'Account created successfully')
#                     return redirect('login')
#         else:
#             messages.warning(request, 'Password do not match')
#             return redirect('register')

#     return render(request, 'accounts/register.html')
