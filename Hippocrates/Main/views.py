from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ListOfPatients.models import ListPatPageOne, ListPatPageTwo
from ListOfPatients.forms import ListPatPageOneForms, ListPatPageTwoForms, FilterListPageOneForms
from InternalStructure.models import InternalStructure, TreatmentResult
from InternalStructure.forms import InternalStructureForms, TreatmentResultForms


def main(request):
    return render(request, 'Main/index.html')


# Отображает лист движения пациентов часть один
def list_pat_part_one(request):
    list_of_pat = ListPatPageOne.objects.all()
    if request.method == 'POST':
        add_pat_form = ListPatPageOneForms(request.POST)
        if add_pat_form.is_valid():
            add_pat_form.save()
            return HttpResponseRedirect(reverse('list_pat_part_one'), {'ListOfPat': list_of_pat})
    else:
        return render(request, 'Main/list_pat_part_one.html', {'ListOfPat': list_of_pat,
                                                               'ListPatPageOneForm': ListPatPageOneForms,
                                                               'FilterListPageOneForm': FilterListPageOneForms})


# Отображает лист движения пациентов часть два
def list_pat_part_two(request):
    list_of_pat = ListPatPageTwo.objects.all()
    if request.method == 'POST':
        add_pat_form = ListPatPageTwoForms(request.POST)
        if add_pat_form.is_valid():
            add_pat_form.save()
            return HttpResponseRedirect(reverse('list_pat_part_two'), {'ListOfPat': list_of_pat})
    else:
        return render(request, 'Main/list_pat_part_two.html', {'ListOfPat': list_of_pat,
                                                               'ListPatPageTwoForm': ListPatPageTwoForms})


# Отображает справочник Внутренняя структура
def internal_structure(request):
    list_of_struct = InternalStructure.objects.all()
    if request.method == 'POST':
        internal_structure_form = InternalStructureForms(request.POST)
        if internal_structure_form.is_valid():
            internal_structure_form.save()
            return HttpResponseRedirect(reverse('internal_structure'), {'list_of_struct': list_of_struct})
    else:
        return render(request, 'Main/internal_structure.html', {'list_of_struct': list_of_struct,
                                                                'internal_structure_form': InternalStructureForms})


# Отображает справочник Результаты лечения
def treatment_result(request):
    list_of_treatment_result = TreatmentResult.objects.all()
    if request.method == 'POST':
        add_list_form = TreatmentResultForms(request.POST)
        if add_list_form.is_valid():
            add_list_form.save()
            return HttpResponseRedirect(reverse('treatment_result'), {'list_of_treatment_result': treatment_result})
    else:
        return render(request, 'Main/treatment_result.html', {'list_of_treatment_result': list_of_treatment_result,
                                                              'treatment_result_form': TreatmentResultForms})
