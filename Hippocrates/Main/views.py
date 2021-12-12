from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ListOfPatients.models import ListPatPageOne, ListPatPageTwo, ListPatView
from ListOfPatients.forms import ListPatPageOneForms, ListPatPageTwoForms, ListPatViewForms
from InternalStructure.models import InternalStructure, TreatmentResult, MedicalInstitution
from InternalStructure.forms import InternalStructureForms, TreatmentResultForms, MedicalInstitutionForms, WhoDirectedForms


def main(request):
    return render(request, 'Main/index.html')


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


# Отображает страницу с данными по определенной модели
def data_page(request, model, rec_form, template, filter_form=None):
    list_of_records = model.objects.all()
    if request.method == 'POST':
        add_list_form = rec_form(request.POST)
        if add_list_form.is_valid():
            add_list_form.save()
            rev = template
            return HttpResponseRedirect(reverse(rev))
    else:
        return render(request, 'Main/' + template + '.html', {'list_of_records': list_of_records,
                                                              'rec_form': rec_form,
                                                              'filter_form': filter_form})

