

from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def resume(request):
    return render(request, 'portfolio/resume.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

from .models import Project

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': all_projects})
