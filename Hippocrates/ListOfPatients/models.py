from django.db import models
from InternalStructure.models import InternalStructure, TreatmentResult, MedicalInstitution


class ListPatPageOne(models.Model):
    date = models.DateField(db_index=True, verbose_name='Дата')
    depart = models.ForeignKey(InternalStructure, on_delete=models.PROTECT, null=True)
    on_start_day = models.IntegerField(verbose_name='Начало дня')
    receive = models.IntegerField(verbose_name='Поступило ')
    transfer_from = models.IntegerField(verbose_name='Переведено из других отделений')
    transfer_to = models.IntegerField(verbose_name='Переведено в другие отделения')
    release_total = models.IntegerField(verbose_name='Выписано всего')
    rel_total_to = models.IntegerField(verbose_name='Выписано в другие отделения')
    die = models.IntegerField(verbose_name='Умерло')
    remain = models.IntegerField(verbose_name='Осталось')

    class Meta():
        verbose_name_plural = 'Лист движения пациентов'
        verbose_name = 'Лист движения пациентов'
        ordering = ['-date']


class ListPatPageTwo(models.Model):
    date = models.DateField(db_index=True, verbose_name='Дата')
    depart = models.ForeignKey(InternalStructure, on_delete=models.PROTECT, null=True)
    history = models.CharField(verbose_name='История болезни', max_length=40)
    full_name = models.CharField(verbose_name='ФИО, поступил', max_length=40)
    transfer_from = models.CharField(verbose_name='ФИО, из других отделений', max_length=40)
    release = models.CharField(verbose_name='ФИО, выписан', max_length=40)
    release_to = models.CharField(verbose_name='ФИО, в другие отделения', max_length=40)
    release_to_depart = models.CharField(verbose_name='ФИО, в другие стационары', max_length=40)
    die = models.CharField(verbose_name='ФИО, умер', max_length=40)

    class Meta():
        verbose_name_plural = 'Лист движения пациентов по фамилиям'
        verbose_name = 'Лист движения пациентов по фамилиям'
        ordering = ['-date']


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
    date_arrived = models.DateField(verbose_name='Дата поступления', null=True, db_index=True)
    date_released = models.DateField(verbose_name='Дата выписки', null=True, db_index=True)
    treatment_result = models.ForeignKey(TreatmentResult, on_delete=models.SET_NULL, null=True,
                                         verbose_name='Результат лечения')
    transfer_to_depart = models.ForeignKey(InternalStructure, on_delete=models.SET_NULL, null=True,
                                           verbose_name='Переведен в другое отделение',related_name='to_depart')
    transfer_to_hospital = models.ForeignKey(MedicalInstitution, on_delete=models.SET_NULL, null=True,
                                             verbose_name='Переведен в дрогое МУ', related_name='to_hosp')

    class Meta:
        verbose_name_plural = 'Список пациентов'
        verbose_name = 'Список пациентов'
        ordering = ['-date_arrived']
