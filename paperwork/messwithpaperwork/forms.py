# Create add record form
from django import forms
from .models import TestSet


class AddTestSetForm(forms.ModelForm):
    nomenclature = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Nomenclature", "class":"form-control"}), label="")
    nsn = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "NSN", "class":"form-control"}), label="")
    model = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Model", "class":"form-control"}), label="")
    serial_number = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Serial", "class":"form-control"}), label="")
    tm_number = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "TM Number", "class":"form-control"}), label="")
    tm_date = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "TM Date", "class":"form-control"}), label="")

    class Meta:
        model = TestSet
        exclude = ("user",)
