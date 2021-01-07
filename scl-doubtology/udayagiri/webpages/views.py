from django.shortcuts import render

def home(request):
    return render(request, 'webpages/home.html')

def about(request):
    return render(request, 'webpages/services.html')


def contact(request):
    return render(request, 'webpages/contact.html')