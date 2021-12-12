from django.contrib import admin
from django.urls import path
from .views import delete_record, edit_record, filter_record
from .models import ListPatView, ListPatPageOne
from .forms import ListPatViewForms, ListPatPageOneForms

urlpatterns = [
        # "Лист движения"
    path('filter_record_list_move/', filter_record, {'model': ListPatPageOne,
                                                     'template': 'list_move',
                                                     'rec_form': ListPatPageOneForms}, name='filter_record_list_move'),
    path('delete_list_move/<int:id_record>/', delete_record, {'model': ListPatPageOne,
                                                              'rev': 'list_move'},
         name='delete_list_move'),
    path('edit_list_move/<int:id_record>/', edit_record, {'model': ListPatPageOne,
                                                          'edit_form': ListPatPageOneForms,
                                                          'template': 'list_move'},
         name='edit_list_move'),
    # "Список пациентов"
    path('filter_record_list_pat_view/', filter_record, {'model': ListPatView,
                                                         'template': 'list_pat_view',
                                                         'rec_form': ListPatViewForms},
         name='filter_record_list_pat_view'),
    path('delete_list_pat_view/<int:id_record>/', delete_record, {'model': ListPatView,
                                                                  'rev': 'list_pat_view'},
         name='delete_list_pat_view'),
    path('edit_list_pat_view/<int:id_record>/', edit_record, {'model': ListPatView,
                                                              'edit_form': ListPatViewForms,
                                                              'template': 'list_pat_view'},
         name='edit_list_pat_view'),
]
