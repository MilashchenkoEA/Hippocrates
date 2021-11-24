from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ListOfPatients.models import ListPatPageOne, ListPatPageTwo
from ListOfPatients.forms import ListPatPageOneForms, ListPatPageTwoForms
from InternalStructure.models import InternalStructure
from InternalStructure.forms import InternalStructureForms


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
                                                               'ListPatPageOneForm': ListPatPageOneForms})


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


#
def internal_structure(request):
    list_of_struct = InternalStructure.objects.all()
    if request.method == 'POST':
        add_internal_struct_form = InternalStructureForms(request.POST)
        if add_internal_struct_form.is_valid():
            add_internal_struct_form.save()
            return HttpResponseRedirect(reverse('internal_structure'), {'list_of_struct': list_of_struct})
        pass
    else:
        return render(request, 'Main/internal_structure.html', {'list_of_struct': list_of_struct,
                                                                'internal_structure_form': InternalStructureForms})
