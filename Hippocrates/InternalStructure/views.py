from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


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
