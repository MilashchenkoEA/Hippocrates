from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ListPatPageOneForms, ListPatPageTwoForms, FilterListPageOneForms
from .models import ListPatPageOne, ListPatPageTwo


def delete_pat(request, id_delete_pat):
    pat_for_del = ListPatPageOne.objects.get(pk=id_delete_pat)
    list_of_pat = ListPatPageOne.objects.all()
    if request.method == 'POST':
        pass
    else:
        pat_for_del.delete()
        return HttpResponseRedirect(reverse('list_pat_part_one'), {'ListOfPat': list_of_pat,
                                                                   'FilterListPageOneForm': FilterListPageOneForms})


def edit_pat(request, id_edit_pat):
    pat_for_edit = ListPatPageOne.objects.get(pk=id_edit_pat)
    list_of_pat = ListPatPageOne.objects.all()
    if request.method == 'POST':
        edit_pat_form = ListPatPageOneForms(request.POST, instance=pat_for_edit)
        if edit_pat_form.is_valid():
            edit_pat_form.save()
            return HttpResponseRedirect(reverse('list_pat_part_one'), {'ListOfPat': list_of_pat})
    else:
        pat_for_edit_form = ListPatPageOneForms(instance=pat_for_edit)
        return render(request, 'Main/list_pat_part_one.html', {'ListOfPat': list_of_pat,
                                                               'ListPatPageOneForm': pat_for_edit_form,
                                                               'FilterListPageOneForm': FilterListPageOneForms})


def delete_pat_two(request, id_delete_pat):
    pat_for_del = ListPatPageTwo.objects.get(pk=id_delete_pat)
    list_of_pat = ListPatPageTwo.objects.all()
    if request.method == 'POST':
        pass
    else:
        pat_for_del.delete()
        return HttpResponseRedirect(reverse('list_pat_part_two'), {'ListOfPat': list_of_pat,
                                                                   'FilterListPageOneForm': FilterListPageOneForms})


def edit_pat_two(request, id_edit_pat):
    pat_for_edit = ListPatPageTwo.objects.get(pk=id_edit_pat)
    list_of_pat = ListPatPageTwo.objects.all()
    if request.method == 'POST':
        edit_pat_form = ListPatPageTwoForms(request.POST, instance=pat_for_edit)
        if edit_pat_form.is_valid():
            edit_pat_form.save()
            return HttpResponseRedirect(reverse('list_pat_part_two'), {'ListOfPat': list_of_pat})
    else:
        pat_for_edit_form = ListPatPageTwoForms(instance=pat_for_edit)
        return render(request, 'Main/list_pat_part_two.html', {'ListOfPat': list_of_pat,
                                                               'ListPatPageTwoForm': pat_for_edit_form,
                                                               'FilterListPageOneForm': FilterListPageOneForms})


# Фильтрация для модели ListPatPageOne (лист движения пациентов страница один) по дате и/или отделению
def list_pat_page_one_filter(request):
    form_filter = FilterListPageOneForms(request.POST)
    if request.method == 'POST':
        if form_filter.is_valid():
            start_day_filter = form_filter.cleaned_data['start_date']
            end_day_filter = form_filter.cleaned_data['end_date']
            depart_filter = form_filter.cleaned_data['depart']
            if depart_filter:
                list_pat_filtered = ListPatPageOne.objects.filter(Depart=depart_filter).filter(
                    Date__range=[start_day_filter, end_day_filter])
            else:
                list_pat_filtered = ListPatPageOne.objects.filter(Date__range=[start_day_filter, end_day_filter])
            return render(request, 'Main/list_pat_part_one.html', {'ListOfPat': list_pat_filtered,
                                                                   'ListPatPageOneForm': ListPatPageOneForms,
                                                                   'FilterListPageOneForm': FilterListPageOneForms})
    else:
        pass
