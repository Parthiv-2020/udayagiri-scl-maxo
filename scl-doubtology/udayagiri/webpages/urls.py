from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('teachers/', views.teacher, name='teacher'),
    path('contact/', views.contact, name='contact'),
]
