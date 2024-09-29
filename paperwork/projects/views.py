from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def projects(request):
    page = 'projects'
    number = 11
    context = {'page': page, 'number': number}
    return render(request, 'projects.html', context)

def project(request, pk):
    return render(request, 'single-project.html')