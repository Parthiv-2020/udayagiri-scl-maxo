from django.urls import path
from . import views

urlpatterns = [
    path('', views.teachers, name="youtubers"),
    path('<int:id>', views.teacher_detail, name="youtubers_detail"),
]
