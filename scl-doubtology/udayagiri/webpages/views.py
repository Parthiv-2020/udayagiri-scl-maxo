from django.shortcuts import render

def home(request):
    return render(request, 'webpages/home.html')

def teacher(request):
    return render(request, 'webpages/teacher.html')


def contact(request):
    return render(request, 'webpages/contact.html')