from django.shortcuts import get_object_or_404, render
from .models import Teacher


def teachers(request):
    teachers = Teacher.objects.order_by('-created_date')
    data = {
        'teachers': teachers
    }
    return render(request, 'teachers/teacher.html', data)


def teacher_detail(request, id):
    teacher = get_object_or_404(Teacher, pk=id)
    data = {
        'teacher': teacher
    }
    return render(request, 'teachers/teacher_detail.html', data)


def search(request):
    teacher = Teacher.objects.order_by('-created_date')


    if 'queryset' in request.GET:
        queryset = request.GET['queryset']
        if queryset:
            teacher = teacher.filter(name__icontains=queryset)


    data = {
        'teachers': teacher,
        'query': queryset
    }
    return render(request, 'teachers/teacher.html', data)