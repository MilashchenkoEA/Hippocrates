from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import InternalStructure
from .forms import InternalStructureForms


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
