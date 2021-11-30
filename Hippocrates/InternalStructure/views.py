from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import InternalStructure, TreatmentResult
from .forms import InternalStructureForms, TreatmentResultForms


def delete_struct(request, id_delete_struct):
    struct_for_del = InternalStructure.objects.get(pk=id_delete_struct)
    list_of_struct = InternalStructure.objects.all()
    if request.method == 'POST':
        pass
    else:
        struct_for_del.delete()
        return HttpResponseRedirect(reverse('internal_structure'), {'list_of_struct': list_of_struct})


def edit_struct(request, id_edit_struct):
    struct_for_edit = InternalStructure.objects.get(pk=id_edit_struct)
    list_of_struct = InternalStructure.objects.all()
    if request.method == 'POST':
        edit_struct_form = InternalStructureForms(request.POST, instance=struct_for_edit)
        if edit_struct_form.is_valid():
            edit_struct_form.save()
            return HttpResponseRedirect(reverse('internal_structure'), {'list_of_struct': list_of_struct})
    else:
        struct_for_edit_form = InternalStructureForms(instance=struct_for_edit)
        return render(request, 'Main/internal_structure.html', {'list_of_struct': list_of_struct,
                                                                'internal_structure_form': struct_for_edit_form})


def delete_treatment_result(request, id_delete_treatment_result):
    for_del = TreatmentResult.objects.get(pk=id_delete_treatment_result)
    list_of_treatment_result = TreatmentResult.objects.all()
    if request.method == 'POST':
        pass
    else:
        for_del.delete()
        return HttpResponseRedirect(reverse('treatment_result'), {'list_of_treatment_result': list_of_treatment_result})


def edit_treatment_result(request, id_edit_treatment_result):
    edit_id = TreatmentResult.objects.get(pk=id_edit_treatment_result)
    list_of_treatment_result = TreatmentResult.objects.all()
    if request.method == 'POST':
        edit_id_form = TreatmentResultForms(request.POST, instance=edit_id)
        if edit_id_form.is_valid():
            edit_id_form.save()
            return HttpResponseRedirect(reverse('treatment_result'),
                                        {'list_of_treatment_result': list_of_treatment_result})
    else:
        edit_id_form = TreatmentResultForms(instance=edit_id)
        return render(request, 'Main/treatment_result.html', {'list_of_treatment_result': list_of_treatment_result,
                                                              'treatment_result_form': edit_id_form})
