from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),         
    path('home/', views.home, name='home2'),   
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('resume/', views.resume, name='resume'),
   
]
