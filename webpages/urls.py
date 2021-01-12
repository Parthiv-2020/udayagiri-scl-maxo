from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('privacy/', views.privacy, name='privacy'),
    path('license/', views.license, name='license')
]
