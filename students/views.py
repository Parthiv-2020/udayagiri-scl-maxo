from django.shortcuts import redirect, render
from .models import Student
from django.contrib import messages
from django.core.mail import send_mail



def student(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']
        state = request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']

        student = Student(first_name=first_name, last_name=last_name, tuber_id=tuber_id, tuber_name=tuber_name,
                              city=city, phone=phone, email=email, state=state, message=message, user_id=user_id)
        student.save()
        subject = f'''
        Hi, {first_name}
        We have received your request, you will receive another confirmation mail soon.

        Happy learning :)
        Tutorvita team
        '''

        send_mail(
            f'TutorVita: Confirmation mail for reaching out {tuber_name}',
            subject,
            'udayagiri.tutorvita@gmail.com',
            [email],
        )

        messages.success(request, 'Thanks for reaching out!')
        return redirect('home')