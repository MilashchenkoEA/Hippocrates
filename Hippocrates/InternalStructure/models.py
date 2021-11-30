from django.db import models


# Модель. "Внутренняя структура"->"Список отделений"
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


# Модель. "Внутренняя структура"->"Список врачей"
class ListOfDoctors(models.Model):
    full_name = models.CharField(verbose_name='ФИО', max_length=40)
    service_number = models.IntegerField(verbose_name="Табельный номер")
    specialization = models.CharField(verbose_name="Специализация", max_length=40)
    depart = models.ForeignKey(InternalStructure, on_delete=models.SET_NULL, null=True,
                               verbose_name='Отделение')

    class Meta():
        verbose_name_plural = 'Список врачей'
        verbose_name = 'Список врачей'
        ordering = ['full_name']


# Модель. "Параметры"->"Результат лечения"
class TreatmentResult(models.Model):
    treatment_result = models.CharField(db_index=True, verbose_name='Результат лечения', max_length=40)

    class Meta():
        verbose_name_plural = 'Результат лечения'
        verbose_name = 'Результат лечения'
        ordering = ['treatment_result']

    def __str__(self):
        return self.treatment_result


# Модель. "Параметры"->"Куда выписан"
class WhereDischarged(models.Model):
    where_discharged = models.CharField(db_index=True, verbose_name='Куда выписан', max_length=40)

    class Meta():
        verbose_name_plural = 'Куда выписан'
        verbose_name = 'Куда выписан'
        ordering = ['where_discharged']

    def __str__(self):
        return self.where_discharged


# Модель. "Параметры"->"Исход лечения"
class TreatmentOutcome(models.Model):
    treatment_outcome = models.CharField(db_index=True, verbose_name='Исход лечения', max_length=40)

    class Meta():
        verbose_name_plural = 'Исход лечения'
        verbose_name = 'Исход лечения'
        ordering = ['treatment_outcome']

    def __str__(self):
        return self.treatment_outcome


# Модель. "Параметры"->"Кто направил"
class WhoDirected(models.Model):
    who_directed = models.CharField(db_index=True, verbose_name='Кто направил', max_length=40)

    class Meta():
        verbose_name_plural = 'Кто направил'
        verbose_name = 'Кто направил'
        ordering = ['who_directed']

    def __str__(self):
        return self.who_directed


# Модель. "Параметры"->"Сроки доставки"
class DeliveryTime(models.Model):
    delivery_time = models.CharField(db_index=True, verbose_name='Сроки доставки', max_length=40)

    class Meta():
        verbose_name_plural = 'Сроки доставки'
        verbose_name = 'Сроки доставки'
        ordering = ['delivery_time']

    def __str__(self):
        return self.delivery_time


# Модель. "Параметры"->"Оглавление МКБ"


# Модель. "Параметры"->"Вскрытие"
class Autopsy(models.Model):
    autopsy = models.CharField(db_index=True, verbose_name='Вскрытие', max_length=40)

    class Meta():
        verbose_name_plural = 'Вскрытие'
        verbose_name = 'Вскрытие'
        ordering = ['autopsy']

    def __str__(self):
        return self.autopsy


# Модель. "Параметры"->"Расхождение при вскрытии"
class DifferenceAutopsy(models.Model):
    difference_autopsy = models.CharField(db_index=True, verbose_name='Расхождение при вскрытии', max_length=40)

    class Meta():
        verbose_name_plural = 'Расхождение при вскрытии'
        verbose_name = 'Расхождение при вскрытии'
        ordering = ['difference_autopsy']

    def __str__(self):
        return self.difference_autopsy


# Модель. "Параметры"->"Финансирование"
class Financing(models.Model):
    financing = models.CharField(db_index=True, verbose_name='Финансирование', max_length=40)

    class Meta():
        verbose_name_plural = 'Финансирование'
        verbose_name = 'Финансирование'
        ordering = ['financing']

    def __str__(self):
        return self.financing


# Модель. "Параметры"->"Группы операций"
class GroupOperation(models.Model):
    group_operation = models.CharField(db_index=True, verbose_name='Группы операций', max_length=40)

    class Meta():
        verbose_name_plural = 'Группы операций'
        verbose_name = 'Группы операций'
        ordering = ['group_operation']

    def __str__(self):
        return self.group_operation


# Модель. "Параметры"->"Наименование операции"
class NameOperation(models.Model):
    name_operation = models.CharField(db_index=True, verbose_name='Наименование операций', max_length=40)
    group_operation = models.ForeignKey(GroupOperation, on_delete=models.SET_NULL, null=True, db_index=True,
                                        verbose_name='Группа операций')

    class Meta():
        verbose_name_plural = 'Наименование операций'
        verbose_name = 'Наименование операций'
        ordering = ['name_operation']

    def __str__(self):
        return self.name_operation


# Модель. "Параметры"->"Обезболивание"
class Anesthesia(models.Model):
    anesthesia = models.CharField(db_index=True, verbose_name='Анестезия', max_length=40)

    class Meta():
        verbose_name_plural = 'Анестезия'
        verbose_name = 'Анестезия'
        ordering = ['anesthesia']

    def __str__(self):
        return self.anesthesia


# Модель. "Параметры"->"Социальное положение"
class SocialStatus(models.Model):
    social_status = models.CharField(db_index=True, verbose_name='Социальный статус', max_length=40)

    class Meta():
        verbose_name_plural = 'Социальный статус'
        verbose_name = 'Социальный статус'
        ordering = ['social_status']

    def __str__(self):
        return self.social_status


# Модель. "Параметры"->"Беременность"
class Pregnancy(models.Model):
    pregnancy = models.CharField(db_index=True, verbose_name='Беременность', max_length=40)

    class Meta():
        verbose_name_plural = 'Беременность'
        verbose_name = 'Беременность'
        ordering = ['pregnancy']

    def __str__(self):
        return self.pregnancy


# Модель. "Параметры"->"Прививка"
class Vaccination(models.Model):
    vaccination = models.CharField(db_index=True, verbose_name='Прививка', max_length=40)

    class Meta():
        verbose_name_plural = 'Прививки'
        verbose_name = 'Прививка'
        ordering = ['vaccination']

    def __str__(self):
        return self.vaccination


# Модель. "Параметры"->"Медицинские учереждения"
class MedicalInstitution(models.Model):
    medical_institution = models.CharField(db_index=True, verbose_name='Медицинское учреждение', max_length=40)

    class Meta():
        verbose_name_plural = 'Медицинские учреждения'
        verbose_name = 'Медицинское учреждение'
        ordering = ['medical_institution']

    def __str__(self):
        return self.medical_institution
