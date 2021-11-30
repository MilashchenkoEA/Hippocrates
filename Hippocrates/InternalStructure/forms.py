from django import forms
from .models import InternalStructure, TreatmentResult


class InternalStructureForms(forms.ModelForm):
    NameDepart = forms.CharField(max_length=40)
    TotalBeds = forms.IntegerField(min_value=0)
    UsedBeds = forms.IntegerField(min_value=0)
    UnusedBeds = forms.IntegerField(min_value=0)

    class Meta:
        model = InternalStructure
        fields = ('NameDepart', 'TotalBeds', 'UsedBeds', 'UnusedBeds')


class TreatmentResultForms(forms.ModelForm):
    treatment_result = forms.CharField(max_length=40)

    class Meta:
        model = TreatmentResult
        fields = ('treatment_result',)