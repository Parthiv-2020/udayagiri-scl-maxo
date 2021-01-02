from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name='maxo-home'),
	path('about/',views.about,name='maxo-about')

]
