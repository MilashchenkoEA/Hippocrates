from django import forms
from .models import InternalStructure


class InternalStructureForms(forms.ModelForm):
    NameDepart = forms.CharField(max_length=40)
    TotalBeds = forms.IntegerField(min_value=0)
    UsedBeds = forms.IntegerField(min_value=0)
    UnusedBeds = forms.IntegerField(min_value=0)

    class Meta:
        model = InternalStructure
        fields = ('NameDepart', 'TotalBeds', 'UsedBeds', 'UnusedBeds')
