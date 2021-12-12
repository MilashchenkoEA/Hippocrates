from django import forms
from .models import ListPatPageOne, ListPatPageTwo, ListPatView
from InternalStructure.models import InternalStructure, MedicalInstitution, TreatmentResult


class ListPatPageOneForms(forms.ModelForm):
    date = forms.DateField()
    depart = forms.ModelChoiceField(queryset=InternalStructure.objects.all())
    on_start_day = forms.IntegerField(min_value=0)
    receive = forms.IntegerField(min_value=0)
    transfer_from = forms.IntegerField(min_value=0)
    transfer_to = forms.IntegerField(min_value=0)
    release_total = forms.IntegerField(min_value=0)
    rel_total_to = forms.IntegerField(min_value=0)
    die = forms.IntegerField(min_value=0)
    remain = forms.IntegerField(min_value=0)

    class Meta:
        model = ListPatPageOne
        fields = ('date', 'depart', 'on_start_day', 'receive', 'transfer_from', 'transfer_to', 'release_total',
                  'rel_total_to', 'die', 'remain')


class ListPatPageTwoForms(forms.ModelForm):
    date = forms.DateField()
    depart = forms.ModelChoiceField(queryset=InternalStructure.objects.all())
    history = forms.CharField(max_length=40, required=False)
    full_name = forms.CharField(max_length=40, required=False)
    transfer_from = forms.CharField(max_length=40, required=False)
    release = forms.CharField(max_length=40, required=False)
    release_to = forms.CharField(max_length=40, required=False)
    release_to_depart = forms.CharField(max_length=40, required=False)
    die = forms.CharField(max_length=40, required=False)

    class Meta:
        model = ListPatPageTwo
        fields = ('date', 'depart', 'history', 'full_name', 'transfer_from', 'release', 'release_to', 'release_to_depart',
                  'die')


class FilterForms(forms.Form):
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
    start_date_arrived = forms.DateField(required=False)
    end_date_arrived = forms.DateField(required=False)
    start_date_released = forms.DateField(required=False)
    end_date_released = forms.DateField(required=False)
    depart = forms.ModelChoiceField(queryset=InternalStructure.objects.all(), required=False)
    full_name = forms.CharField(max_length=40, required=False)
    arrived_from_depart = forms.ModelChoiceField(queryset=InternalStructure.objects.all(), required=False)
    arrived_from_hosp = forms.ModelChoiceField(queryset=MedicalInstitution.objects.all(), required=False)
    treatment_result = forms.ModelChoiceField(queryset=TreatmentResult.objects.all(), required=False)
    transfer_to_depart = forms.ModelChoiceField(queryset=InternalStructure.objects.all(), required=False)
    transfer_to_hospital = forms.ModelChoiceField(queryset=MedicalInstitution.objects.all(), required=False)
    # service_number
    # specialization
    # group_operation


# Форма. "Движение больных"->"Список пациентов"
class ListPatViewForms(forms.ModelForm):
    depart = forms.ModelChoiceField(queryset=InternalStructure.objects.all())
    history = forms.CharField(max_length=40)
    full_name = forms.CharField(max_length=40)
    arrived_from_depart = forms.ModelChoiceField(queryset=InternalStructure.objects.all(), required=False)
    arrived_from_hosp = forms.ModelChoiceField(queryset=MedicalInstitution.objects.all(), required=False)
    date_arrived = forms.DateField(required=False)
    date_released = forms.DateField(required=False)
    treatment_result = forms.ModelChoiceField(queryset=TreatmentResult.objects.all())
    transfer_to_depart = forms.ModelChoiceField(queryset=InternalStructure.objects.all(), required=False)
    transfer_to_hospital = forms.ModelChoiceField(queryset=MedicalInstitution.objects.all(), required=False)

    class Meta:
        model = ListPatView
        fields = ('depart', 'history', 'full_name', 'arrived_from_depart', 'arrived_from_hosp', 'date_arrived',
                  'date_released', 'treatment_result', 'transfer_to_depart', 'transfer_to_hospital')
