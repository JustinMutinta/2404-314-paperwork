from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import TestSet

organization = "Bravo Co. 449th ASB"
remarks = """
            Words to be entered in the remarks section of the 314
            Making sure that line 2 works
"""


def home(request):
    testSets = TestSet.objects.all()
    return render(request, 'home.html', {'testSets': testSets})


def testSet(request, pk):
    testSet = TestSet.objects.get(id=pk)
    return render(request, 'testSet.html', {'testSet': testSet})


def delete_testset(request, pk):
    delete_it = TestSet.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, "You have deleted the test set successfully")
    return redirect('home')