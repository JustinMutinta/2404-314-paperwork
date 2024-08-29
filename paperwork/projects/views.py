from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def projects(request):
    return HttpResponse('Here are our Products')

def project(request, pk):
    return HttpResponse('Here is a single Product' + ' ' + str(pk))