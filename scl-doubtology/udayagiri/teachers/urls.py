from django.urls import path
from . import views

urlpatterns = [
    path('', views.teachers, name="teacher"),
    path('<int:id>', views.teacher_detail, name="teacher_detail"),
]
