from django.shortcuts import get_object_or_404, render
from .models import Teacher
from django.contrib.auth.decorators import login_required
from .filters import TeacherFilter

@login_required
def teachers(request):
    
    teachers = Teacher.objects.order_by('-created_date')
    teacher_filter = TeacherFilter(request.GET, queryset=teachers)
    teachers = teacher_filter.qs
    
    data = {
        'teachers': teachers,
        'teacher_filter': teacher_filter
    }
    return render(request, 'teachers/teacher.html', data)


@login_required
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