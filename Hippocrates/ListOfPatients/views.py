from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .forms import ListPatPageOneForms
from .models import ListPatPageOne


class ListPatPageOneCreateView(CreateView):
    template_name = 'ListOfPatients/RecordInList.html'
    form_class = ListPatPageOneForms
    success_url = '/listpat/'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


def index(request):
    list_of_pat = ListPatPageOne.objects.all()
    return render(request, 'ListOfPatients/ListReview.html', {'ListOfPat': list_of_pat})
