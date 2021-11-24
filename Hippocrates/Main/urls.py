from django.urls import path
from .views import main, list_pat_part_one, list_pat_part_two, internal_structure


urlpatterns = [
    path('', main, name='main'),
    path('list_pat_part_one/', list_pat_part_one, name='list_pat_part_one'),
    path('list_pat_part_two/', list_pat_part_two, name='list_pat_part_two'),
    path('internal_structure/', internal_structure, name='internal_structure'),
]
