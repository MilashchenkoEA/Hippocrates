from django.contrib import admin
from django.urls import path

from .views import edit_struct, delete_struct, delete_treatment_result, edit_treatment_result


urlpatterns = [
    path('delete_struct/<int:id_delete_struct>/', delete_struct, name='delete_struct'),
    path('edit_struct/<int:id_edit_struct>/', edit_struct, name='edit_struct'),

    path('delete_treatment_result/<int:id_delete_treatment_result>/', delete_treatment_result, name='delete_treatment_result'),
    path('edit_treatment_result/<int:id_edit_treatment_result>/', edit_treatment_result, name='edit_treatment_result'),
]
