from django.contrib import admin
from django.urls import path

from .views import edit_struct, delete_struct


urlpatterns = [
    path('delete_struct/<int:id_delete_struct>/', delete_struct, name='delete_struct'),
    path('edit_struct/<int:id_edit_struct>/', edit_struct, name='edit_struct'),
]
