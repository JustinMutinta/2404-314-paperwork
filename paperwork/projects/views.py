from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

projectsList = [
    {
        'id' : '1',
        'title' : "Ecommerce Website",
        'description': 'Fully Functional ecommerce website'
    },
    {
        'id' : '2',
        'title' : "Portfolio Website",
        'description': 'This was a project where I built out my portfolio'
    },
    {
        'id' : '3',
        'title' : "Social Network",
        'description': 'Awesome open source project I am still working on'
    },
]


def projects(request):
    page = 'projects'
    number = 11
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, 'projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'single-project.html', {'project':projectObj})