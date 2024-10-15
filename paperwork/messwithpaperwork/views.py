import PyPDF2
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
    testSet = TestSet.objects.get(id=pk)
    print_form_314(testSet)
    print_form_2404(testSet)
    messages.success(request, f"You have printed {testSet.nomenclature} successfully")
    return redirect('home')


def print_form_314(testSet):
    data = {
        'reg[0]': 'Registration Number1',
        'admin[0]': 'Adminstration no.1',
        'nomen[0]': testSet.nomenclature,
        'model[0]': testSet.model,
        'at[0]': organization,
        'TextField2[372]': remarks,
        'model[1]': testSet.model,
        'reg[1]': 'None reg',
        'admin[1]': 'None admin',
        'nomen[1]': testSet.nomenclature,
        'model[1]': testSet.model,
        'at[1]': organization,
    }

    reader = PyPDF2.PdfReader("messwithpaperwork/outputforms/templates/dd0314.pdf")
    writer = PyPDF2.PdfWriter()

    page = reader.pages[0]

    writer.add_page(page)

    writer.update_page_form_field_values(writer.pages[0], data)

    with open(f"messwithpaperwork/outputforms/outputs/DD314_{testSet.nomenclature}_{testSet.serial_number}.pdf", "wb") as output_stream:
        writer.write(output_stream)



def print_form_2404(testSet):
    data = {
        'ORGANIZ[0]': organization,
        'REGISTRAT[0]': f"{testSet.nsn} / {testSet.serial_number}",
        'NOMENMODEL[0]': f"{testSet.nomenclature} {testSet.model}",
        'TMNUM_A[0]': testSet.tm_number,
        'TMDATE_A[0]': testSet.tm_date
    }

    reader = PyPDF2.PdfReader("messwithpaperwork/outputforms/templates/DA2404.pdf")
    writer = PyPDF2.PdfWriter()

    page = reader.pages[0]

    writer.add_page(page)

    writer.update_page_form_field_values(writer.pages[0], data)

    with open(f"messwithpaperwork/outputforms/outputs/DA2404_{testSet.nomenclature}_{testSet.serial_number}.pdf", "wb") as output_stream:
        writer.write(output_stream)