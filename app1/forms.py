from django import forms
from .models import BeratBadan

class BeratForm(forms.ModelForm):
    class Meta:
        model = BeratBadan
        fields = ['tanggal', 'berat']
        widgets = {
            "tanggal": forms.DateInput(attrs={"class": "form-control"}),
            "berat": forms.NumberInput(attrs={"class": "form-control"}),
        }
