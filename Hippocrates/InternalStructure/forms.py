from django import forms
from .models import InternalStructure, TreatmentResult, WhereDischarged, WhoDirected, DeliveryTime, Autopsy, \
    DifferenceAutopsy, Financing, GroupOperation, NameOperation, Anesthesia, SocialStatus, Pregnancy, Vaccination, \
    MedicalInstitution


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


# Форма. "Параметры"->"Куда выписан"
class WhereDischargedForms(forms.ModelForm):
    where_discharged = forms.CharField(max_length=40)

    class Meta:
        model = WhereDischarged
        fields = ('where_discharged',)


# Форма. "Параметры"->"Кто направил"
class WhoDirectedForms(forms.ModelForm):
    who_directed = forms.CharField(max_length=40)

    class Meta:
        model = WhoDirected
        fields = ('who_directed',)


# Форма. "Параметры"->"Сроки доставки"
class DeliveryTimeForms(forms.ModelForm):
    delivery_time = forms.CharField(max_length=40)

    class Meta:
        model = DeliveryTime
        fields = ('delivery_time',)


# Форма. "Параметры"->"Оглавление МКБ"


# Форма. "Параметры"->"Вскрытие"
class AutopsyForms(forms.ModelForm):
    autopsy = forms.CharField(max_length=40)

    class Meta:
        model = Autopsy
        fields = ('autopsy',)


# Форма. "Параметры"->"Расхождение при вскрытии"
class DifferenceAutopsyForms(forms.ModelForm):
    difference_autopsy = forms.CharField(max_length=40)

    class Meta:
        model = DifferenceAutopsy
        fields = ('difference_autopsy',)


# Форма. "Параметры"->"Финансирование"
class FinancingForms(forms.ModelForm):
    financing = forms.CharField(max_length=40)

    class Meta:
        model = Financing
        fields = ('financing',)


# Форма. "Параметры"->"Группы операций"
class GroupOperationForms(forms.ModelForm):
    group_operation = forms.CharField(max_length=40)

    class Meta:
        model = GroupOperation
        fields = ('group_operation',)


# Форма. "Параметры"->"Наименование операции"
class NameOperationForms(forms.ModelForm):
    name_operation = forms.CharField(max_length=40)
    group_operation = forms.ModelChoiceField(queryset=GroupOperation.objects.all())

    class Meta:
        model = NameOperation
        fields = ('name_operation', 'group_operation',)


# Форма. "Параметры"->"Обезболивание"
class AnesthesiaForms(forms.ModelForm):
    anesthesia = forms.CharField(max_length=40)

    class Meta:
        model = Anesthesia
        fields = ('anesthesia',)


# Форма. "Параметры"->"Социальное положение"
class SocialStatusForms(forms.ModelForm):
    social_status = forms.CharField(max_length=40)

    class Meta:
        model = SocialStatus
        fields = ('social_status',)


# Форма. "Параметры"->"Беременность"
class PregnancyForms(forms.ModelForm):
    pregnancy = forms.CharField(max_length=40)

    class Meta:
        model = Pregnancy
        fields = ('pregnancy',)


# Форма. "Параметры"->"Прививка"
class VaccinationForms(forms.ModelForm):
    vaccination = forms.CharField(max_length=40)

    class Meta:
        model = Vaccination
        fields = ('vaccination',)


# Форма. "Параметры"->"Медицинские учереждения"
class MedicalInstitutionForms(forms.ModelForm):
    medical_institution = forms.CharField(max_length=40)

    class Meta:
        model = MedicalInstitution
        fields = ('medical_institution',)
