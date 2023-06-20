from django.shortcuts import render
from .models import Project

def all_blogs(request):
    projects = Project.objects.all()
    return render(request, 'blog/all_blogs.html', {'projects': projects})