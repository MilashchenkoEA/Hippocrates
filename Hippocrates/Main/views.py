from django.shortcuts import render
from ListOfPatients.models import ListPatPageOne


def main(request):
    list_of_pat = ListPatPageOne.objects.all()
    return render(request, 'Main/index.html', {'ListOfPat': list_of_pat})

# Отображает лист движения пациентов часть один
def list_pat_part_one(request):
    list_of_pat = ListPatPageOne.objects.all()
    return render(request, 'Main/list_pat_part_one.html', {'ListOfPat': list_of_pat})
