from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import TestSet
from .forms import AddTestSetForm

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


def add_testset(request):
    form = AddTestSetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_testset = form.save()
            messages.success(request, "Test Set Added...")
            return redirect('home')
    return render(request, 'add_testset.html', {'form':form})


def edit_testset(request, pk):
    current_record = TestSet.objects.get(id=pk)
    form = AddTestSetForm(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request, f"Test set {current_record} has been updated")
        return redirect('home')
    return render(request, 'edit_testset.html', {'form':form})


def print_testset(request, pk):
    print("Test")
    messages.success(request, "You have printed ___ successfully")
    return redirect('home')