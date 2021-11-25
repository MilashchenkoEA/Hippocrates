from django.db import models

# Внутренняя структура
class InternalStructure(models.Model):
    NameDepart = models.CharField(db_index=True, verbose_name='Отделение', max_length=40)
    TotalBeds = models.IntegerField(verbose_name='Всего коек')
    UsedBeds = models.IntegerField(verbose_name='Занято коек')
    UnusedBeds = models.IntegerField(verbose_name='Свободно коек')

    class Meta():
        verbose_name_plural = 'Внутренняя структура'
        verbose_name = 'Внутренняя структура'
        ordering = ['NameDepart']

    def __str__(self):
        return self.NameDepart