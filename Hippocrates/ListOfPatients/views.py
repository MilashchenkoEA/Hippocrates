from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from .forms import ListPatPageOneForms, ListPatPageTwoForms
from .models import ListPatPageOne, ListPatPageTwo


class ListPatPageOneCreateView(CreateView):
    template_name = 'ListOfPatients/RecordInList.html'
    form_class = ListPatPageOneForms
    success_url = '/list_pat/'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


def list_pat_page_one(request):
    list_of_pat = ListPatPageOne.objects.all()
    return render(request, 'ListOfPatients/ListReview.html', {'ListOfPat': list_of_pat})


def delete_pat(request, id_delete_pat):
    pat_for_del = ListPatPageOne.objects.get(pk=id_delete_pat)
    list_of_pat = ListPatPageOne.objects.all()
    if request.method == 'POST':
        pass
    else:
        pat_for_del.delete()
        return HttpResponseRedirect(reverse('list_pat_part_one'), {'ListOfPat': list_of_pat})


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
                                                               'ListPatPageOneForm': pat_for_edit_form})

def delete_pat_two(request, id_delete_pat):
    pat_for_del = ListPatPageTwo.objects.get(pk=id_delete_pat)
    list_of_pat = ListPatPageTwo.objects.all()
    if request.method == 'POST':
        pass
    else:
        pat_for_del.delete()
        return HttpResponseRedirect(reverse('list_pat_part_two'), {'ListOfPat': list_of_pat})


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
                                                               'ListPatPageTwoForm': pat_for_edit_form})