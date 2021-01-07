from django.urls import path
from . import views
from students.views import student

urlpatterns = [
    path('', views.teachers, name="teacher"),
    path('<int:id>/', views.teacher_detail, name="teacher_detail"),
    path('search/', views.search, name="search"),
    path('student/', student, name="student")

]
