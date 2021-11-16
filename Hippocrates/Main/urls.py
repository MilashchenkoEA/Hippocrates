from django.urls import path
from .views import main
from .views import list_pat_part_one


urlpatterns = [
    path('', main, name='Main'),
    path('list_pat_part_one/', list_pat_part_one, name='list_pat_part_one'),
]
