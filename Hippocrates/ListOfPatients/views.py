from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ListPatPageOneForms, ListPatPageTwoForms, FilterForms, ListPatViewForms
from .models import ListPatPageOne, ListPatPageTwo, ListPatView


def delete_record(request, id_record, rev, model):
    rec_for_del = model.objects.get(pk=id_record)
    list_of_records = model.objects.all()
    if request.method == 'POST':
        pass
    else:
        rec_for_del.delete()
        return HttpResponseRedirect(reverse(rev), {'list_of_records': list_of_records})


def edit_record(request, id_record, model, edit_form, template):
    edit_id = model.objects.get(pk=id_record)
    list_of_records = model.objects.all()
    if request.method == 'POST':
        edit_id_form = edit_form(request.POST, instance=edit_id)
        if edit_id_form.is_valid():
            edit_id_form.save()
            rev = template
            return HttpResponseRedirect(reverse(rev),
                                        {'list_of_records': list_of_records})
    else:
        edit_id_form = edit_form(instance=edit_id)
        return render(request, 'Main/' + template + '.html', {'list_of_records': list_of_records,
                                                              'rec_form': edit_id_form})


# Фильтрация
def filter_record(request, model, template, rec_form):
    filter_form = FilterForms(request.POST)
    if request.method == 'POST':
        if filter_form.is_valid():
            start_day_val = filter_form.cleaned_data['start_date']
            end_day_val = filter_form.cleaned_data['end_date']
            depart_val = filter_form.cleaned_data['depart']
            full_name_val = filter_form.cleaned_data['full_name']
            arrived_from_depart_val = filter_form.cleaned_data['arrived_from_depart']
            arrived_from_hosp_val = filter_form.cleaned_data['arrived_from_hosp']
            start_date_arrived_val = filter_form.cleaned_data['start_date_arrived']
            end_date_arrived_val = filter_form.cleaned_data['end_date_arrived']
            treatment_result_val = filter_form.cleaned_data['treatment_result']
            start_date_released_val = filter_form.cleaned_data['start_date_released']
            end_date_released_val = filter_form.cleaned_data['end_date_released']
            q = model.objects.all()
            if depart_val:
                q = q.filter(depart=depart_val)
            if start_day_val and end_day_val:
                q = q.filter(date__range=[start_day_val, end_day_val])
            if full_name_val:
                q = q.filter(full_name__istartswith=full_name_val)
            if arrived_from_depart_val:
                q = q.filter(arrived_from_depart=arrived_from_depart_val)
            if arrived_from_hosp_val:
                q = q.filter(arrived_from_hosp=arrived_from_hosp_val)
            if start_date_arrived_val and end_date_arrived_val:
                q = q.filter(date_arrived__range=[start_date_arrived_val, end_date_arrived_val])
            if treatment_result_val:
                q = q.filter(treatment_result=treatment_result_val)
            if start_date_released_val and end_date_released_val:
                q = q.filter(date_released__range=[start_date_released_val, end_date_released_val])


            return render(request, 'Main/' + template + '.html', {'list_of_records': q,
                                                                  'rec_form': rec_form,
                                                                  'filter_form': filter_form})
    else:
        pass
