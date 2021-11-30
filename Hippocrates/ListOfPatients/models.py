from django.db import models
from InternalStructure.models import InternalStructure, TreatmentResult, MedicalInstitution


class ListPatPageOne(models.Model):
    Date = models.DateField(db_index=True, verbose_name='Дата')
    Depart = models.ForeignKey(InternalStructure, on_delete=models.PROTECT, null=True)
    OnStartDay = models.IntegerField(verbose_name='Начало дня')
    Receive = models.IntegerField(verbose_name='Поступило ')
    TransferFrom = models.IntegerField(verbose_name='Переведено из других отделений')
    TransferTo = models.IntegerField(verbose_name='Переведено в другие отделения')
    ReleaseTotal = models.IntegerField(verbose_name='Выписано всего')
    RelTotalTo = models.IntegerField(verbose_name='Выписано в другие отделения')
    Die = models.IntegerField(verbose_name='Умерло')
    Remain = models.IntegerField(verbose_name='Осталось')

    class Meta():
        verbose_name_plural = 'Лист движения пациентов'
        verbose_name = 'Лист движения пациентов'
        ordering = ['-Date']


class ListPatPageTwo(models.Model):
    Date = models.DateField(db_index=True, verbose_name='Дата')
    Depart = models.ForeignKey(InternalStructure, on_delete=models.PROTECT, null=True)
    History = models.CharField(verbose_name='История болезни', max_length=40)
    FNL = models.CharField(verbose_name='ФИО, поступил', max_length=40)
    TransferFrom = models.CharField(verbose_name='ФИО, из других отделений', max_length=40)
    Release = models.CharField(verbose_name='ФИО, выписан', max_length=40)
    ReleaseTo = models.CharField(verbose_name='ФИО, в другие отделения', max_length=40)
    ReleaseToDepart = models.CharField(verbose_name='ФИО, в другие стационары', max_length=40)
    Die = models.CharField(verbose_name='ФИО, умер', max_length=40)

    class Meta():
        verbose_name_plural = 'Лист движения пациентов по фамилиям'
        verbose_name = 'Лист движения пациентов по фамилиям'
        ordering = ['-Date']


# Модель. "Движение больных"->"Список пациентов"
class ListPatView(models.Model):
    depart = models.ForeignKey(InternalStructure, on_delete=models.SET_NULL, null=True,
                               verbose_name='Отделение', related_name='depart')
    history = models.CharField(verbose_name='История болезни', max_length=40)
    full_name = models.CharField(verbose_name='ФИО', max_length=40)
    arrived_from_depart = models.ForeignKey(InternalStructure, on_delete=models.SET_NULL, null=True,
                                            verbose_name='Поступил из отделения', related_name='from_depart')
    arrived_from_hosp = models.ForeignKey(MedicalInstitution, on_delete=models.SET_NULL, null=True,
                                          verbose_name='Поступил из другого МУ', related_name='from_hosp')
    date_arrived = models.DateField(verbose_name='Дата поступления', db_index=True)
    date_release = models.DateField(verbose_name='Дата выписки', db_index=True)
    treatment_result = models.ForeignKey(TreatmentResult, on_delete=models.SET_NULL, null=True,
                                         verbose_name='Результат лечения')
    transfer_to_depart = models.ForeignKey(InternalStructure, on_delete=models.SET_NULL, null=True,
                                           verbose_name='Переведен в другое отделение', related_name='to_depart')
    transfer_to_hospital = models.ForeignKey(MedicalInstitution, on_delete=models.SET_NULL, null=True,
                                             verbose_name='Поступил из другого МУ', related_name='to_hosp')

    class Meta():
        verbose_name_plural = 'Список пациентов'
        verbose_name = 'Список пациентов'
        ordering = ['-date_arrived']
