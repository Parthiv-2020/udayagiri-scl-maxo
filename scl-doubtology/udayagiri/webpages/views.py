from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.contrib.auth.decorators import login_required

# def landing_page(request):
#     return render(request, 'webpages/index.html')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'webpages/home.html')
    else:
        return render(request, 'webpages/index.html')

    

def about(request):
    return render(request, 'webpages/about.html')

@login_required
def team(request):
    return render(request, 'webpages/team.html')

@login_required
def privacy(request):
    return render(request, 'webpages/privacy.html')

@login_required
def license(request):
    return render(request, 'webpages/license.html')

@login_required
def contact(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        comment = request.POST['message']
        message = Contact()
        message.name = name
        message.email = email
        message.subject = subject
        message.comments = comment
        message.save()
        messages.success(request, 'Your response is recorded')
        return redirect('contact')
    else:
        return render(request, 'webpages/contact.html',{})
    
