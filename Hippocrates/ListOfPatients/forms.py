from django import forms
from .models import ListPatPageOne, ListPatPageTwo
from InternalStructure.models import InternalStructure


class ListPatPageOneForms(forms.ModelForm):
    Date = forms.DateField()
    Depart = forms.ModelChoiceField(queryset=InternalStructure.objects.all())
    OnStartDay = forms.IntegerField(min_value=0)
    Receive = forms.IntegerField(min_value=0)
    TransferFrom = forms.IntegerField(min_value=0)
    TransferTo = forms.IntegerField(min_value=0)
    ReleaseTotal = forms.IntegerField(min_value=0)
    RelTotalTo = forms.IntegerField(min_value=0)
    Die = forms.IntegerField(min_value=0)
    Remain = forms.IntegerField(min_value=0)

    class Meta:
        model = ListPatPageOne
        fields = ('Date', 'Depart', 'OnStartDay', 'Receive', 'TransferFrom', 'TransferTo', 'ReleaseTotal',
                  'RelTotalTo', 'Die', 'Remain')


class ListPatPageTwoForms(forms.ModelForm):
    Date = forms.DateField()
    Depart = forms.ModelChoiceField(queryset=InternalStructure.objects.all())
    History = forms.CharField(max_length=40, required=False)
    FNL = forms.CharField(max_length=40, required=False)
    TransferFrom = forms.CharField(max_length=40, required=False)
    Release = forms.CharField(max_length=40, required=False)
    ReleaseTo = forms.CharField(max_length=40, required=False)
    ReleaseToDepart = forms.CharField(max_length=40, required=False)
    Die = forms.CharField(max_length=40, required=False)

    class Meta:
        model = ListPatPageTwo
        fields = ('Date', 'Depart', 'History', 'FNL', 'TransferFrom', 'Release', 'ReleaseTo', 'ReleaseToDepart',
                  'Die')


class FilterListPageOneForms(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()
    depart = forms.ModelChoiceField(queryset=InternalStructure.objects.all(), required=False)
