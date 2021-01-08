from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def home(request):
    return render(request, 'webpages/home.html')

def about(request):
    return render(request, 'webpages/about.html')

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
    
