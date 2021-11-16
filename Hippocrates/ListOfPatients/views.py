from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from .forms import ListPatPageOneForms
from .models import ListPatPageOne


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
