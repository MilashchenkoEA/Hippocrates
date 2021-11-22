from django.db import models


class ListPatPageOne(models.Model):
    Date = models.DateField(db_index=True, verbose_name='Дата')
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
