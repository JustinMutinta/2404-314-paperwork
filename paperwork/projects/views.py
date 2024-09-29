from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def projects(request):
    msg = 'Hello, you are on the projects view'
    return render(request, 'projects.html', {'message': msg})

def project(request, pk):
    return render(request, 'single-project.html')