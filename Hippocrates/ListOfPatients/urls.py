from django.contrib import admin
from django.urls import path

from .views import index

from .views import ListPatPageOneCreateView

urlpatterns = [
    path('recordinlist/', ListPatPageOneCreateView.as_view(), name='RecordInList'),
    path('listpat/', index),
]
