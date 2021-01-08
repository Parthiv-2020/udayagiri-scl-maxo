from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'webpages/home.html')

def teacher(request):
    return render(request, 'webpages/teacher.html')


def contact(request):
	# if request.POST:
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     subject = request.POST['subject']
    #     comment = request.POST['message']
    #     comment = name + " with the email, " + email + ", sent the following message:\n\n" + comment
    #     send_mail(subject, comment, None, ['18praneeth@gmail.com'])
    #     message = Contact()
    #     message.name = name
    #     message.email = email
    #     message.subject = subject
    #     message.comments = comment
    #     message.save()
    #     if email:
    #         messages.success(request, 'Thank you for showing interest in '
    #                                   'the ABC, We will contact you '
    #                                   'within '
    #                                   '24hrs.')
    #     else:
    #         pass
    #     return redirect(request.META['HTTP_REFERER'])
    # else:
    return render(request, 'webpages/contact.html',{})
    
