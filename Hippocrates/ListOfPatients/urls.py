from django.contrib import admin
from django.urls import path

from .views import list_pat_page_one, delete_pat

from .views import ListPatPageOneCreateView

urlpatterns = [
    path('recordinlist/', ListPatPageOneCreateView.as_view(), name='recordInList'),
    path('list_pat/', list_pat_page_one, name='list_pat'),
    path('delete_pat/<int:id_delete_pat>/', delete_pat, name='delete_pat'),
]
