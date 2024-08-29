from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def projects(request):
    return HttpResponse('Here are our Products')

def project(request, pk):
    return HttpResponse('Here is a single Product' + ' ' + str(pk))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects, name="projects"),
    path('project/<str:pk>/', project, name="project"),
]
