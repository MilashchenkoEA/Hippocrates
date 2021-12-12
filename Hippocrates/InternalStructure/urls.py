from django.contrib import admin
from django.urls import path

from .views import delete_record, edit_record
from .models import MedicalInstitution, InternalStructure, TreatmentResult, WhoDirected, DeliveryTime, Autopsy, \
    GroupOperation
from .forms import MedicalInstitutionForms, InternalStructureForms, TreatmentResultForms, WhoDirectedForms, \
    DeliveryTimeForms, AutopsyForms, GroupOperationForms

urlpatterns = [
    path('delete_internal_structure/<int:id_record>/', delete_record, {'model': InternalStructure,
                                                                       'rev': 'internal_structure'},
         name='delete_internal_structure'),
    path('edit_internal_structure/<int:id_record>/', edit_record, {'model': InternalStructure,
                                                                   'edit_form': InternalStructureForms,
                                                                   'template': 'internal_structure'},
         name='edit_internal_structure'),

    path('delete_treatment_result/<int:id_record>/', delete_record, {'model': TreatmentResult,
                                                                     'rev': 'treatment_result'},
         name='delete_treatment_result'),
    path('edit_treatment_result/<int:id_record>/', edit_record, {'model': TreatmentResult,
                                                                 'edit_form': TreatmentResultForms,
                                                                 'template': 'treatment_result'},
         name='edit_treatment_result'),

    path('delete_medical_institution/<int:id_record>/', delete_record, {'model': MedicalInstitution,
                                                                        'rev': 'medical_institution'},
         name='delete_medical_institution'),
    path('edit_medical_institution/<int:id_record>/', edit_record, {'model': MedicalInstitution,
                                                                    'edit_form': MedicalInstitutionForms,
                                                                    'template': 'medical_institution'},
         name='edit_medical_institution'),

    path('delete_who_directed/<int:id_record>/', delete_record, {'model': WhoDirected,
                                                                 'rev': 'who_directed'},
         name='delete_who_directed'),
    path('edit_who_directed/<int:id_record>/', edit_record, {'model': WhoDirected,
                                                             'edit_form': WhoDirectedForms,
                                                             'template': 'who_directed'},
         name='edit_who_directed'),

    path('delete_delivery_time/<int:id_record>/', delete_record, {'model': DeliveryTime,
                                                                  'rev': 'delivery_time'},
         name='delete_delivery_time'),
    path('edit_delivery_time/<int:id_record>/', edit_record, {'model': DeliveryTime,
                                                              'edit_form': DeliveryTimeForms,
                                                              'template': 'delivery_time'},
         name='edit_delivery_time'),

    path('delete_autopsy/<int:id_record>/', delete_record, {'model': Autopsy,
                                                            'rev': 'autopsy'},
         name='delete_autopsy'),
    path('edit_autopsy/<int:id_record>/', edit_record, {'model': Autopsy,
                                                        'edit_form': AutopsyForms,
                                                        'template': 'autopsy'},
         name='edit_autopsy'),

    path('delete_group_operation/<int:id_record>/', delete_record, {'model': GroupOperation,
                                                                    'rev': 'group_operation'},
         name='delete_group_operation'),
    path('group_operation/<int:id_record>/', edit_record, {'model': GroupOperation,
                                                           'edit_form': GroupOperationForms,
                                                           'template': 'group_operation'},
         name='edit_group_operation'),
]
