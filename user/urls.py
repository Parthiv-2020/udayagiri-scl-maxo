from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.user_profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('forgot-password/', views.user_forgot_password, name='forgot_password'),
    path('logout/', views.user_logout, name='logout')
]
