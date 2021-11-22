from django.contrib import admin
from django.urls import path

from .views import list_pat_page_one, delete_pat, edit_pat, delete_pat_two, edit_pat_two

from .views import ListPatPageOneCreateView

urlpatterns = [
    path('delete_pat/<int:id_delete_pat>/', delete_pat, name='delete_pat'),
    path('edit_pat/<int:id_edit_pat>/', edit_pat, name='edit_pat'),
    path('delete_pat_two/<int:id_delete_pat>/', delete_pat_two, name='delete_pat_two'),
    path('edit_pat_two/<int:id_edit_pat>/', edit_pat_two, name='edit_pat_two'),
]
