from django.urls import path
from .views import main, list_pat_part_two, data_page
from InternalStructure.models import WhoDirected, MedicalInstitution, TreatmentResult, InternalStructure, DeliveryTime, \
    Autopsy, GroupOperation
from InternalStructure.forms import WhoDirectedForms, MedicalInstitutionForms, TreatmentResultForms, \
    InternalStructureForms, DeliveryTimeForms, AutopsyForms, GroupOperationForms
from ListOfPatients.models import ListPatView, ListPatPageOne
from ListOfPatients.forms import ListPatViewForms, ListPatPageOneForms, FilterForms

urlpatterns = [
    path('', main, name='main'),
    # "Движение"->"Движение по датам"
    path('list_move/', data_page, {'model': ListPatPageOne, 'rec_form': ListPatPageOneForms,
                                   'filter_form': FilterForms,
                                   'template': 'list_move'}, name='list_move'),
    path('list_pat_part_two/', list_pat_part_two, name='list_pat_part_two'),
    # "Движение"->"Список больных"
    path('list_pat_view/', data_page, {'model': ListPatView, 'rec_form': ListPatViewForms,
                                       'filter_form': FilterForms,
                                       'template': 'list_pat_view'}, name='list_pat_view'),
    # "Внутренняя структура"->"Список отделений"
    path('internal_structure/', data_page, {'model': InternalStructure, 'rec_form': InternalStructureForms,
                                            'template': 'internal_structure'}, name='internal_structure'),
    path('treatment_result/', data_page, {'model': TreatmentResult, 'rec_form': TreatmentResultForms,
                                          'template': 'treatment_result'}, name='treatment_result'),
    path('medical_institution/', data_page, {'model': MedicalInstitution, 'rec_form': MedicalInstitutionForms,
                                             'template': 'medical_institution'}, name='medical_institution'),
    path('who_directed/', data_page, {'model': WhoDirected, 'rec_form': WhoDirectedForms, 'template': 'who_directed'},
         name='who_directed'),

    path('delivery_time/', data_page,
         {'model': DeliveryTime, 'rec_form': DeliveryTimeForms, 'template': 'delivery_time'},
         name='delivery_time'),

    path('autopsy/', data_page, {'model': Autopsy, 'rec_form': AutopsyForms, 'template': 'autopsy'}, name='autopsy'),
    path('group_operation/', data_page, {'model': GroupOperation, 'rec_form': GroupOperationForms,
                                         'template': 'group_operation'}, name='group_operation'),
]
