from django.db import models


class Subdivision(models.Model):
    name = models.CharField(max_length=200, verbose_name='Подразделение')

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=70, verbose_name='Должность')

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=70, verbose_name='Отдел')

    def __str__(self):
        return self.name

class Employe(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя сотрудника")
    second_name = models.CharField(max_length=100, verbose_name="Фамилия сотрудника")
    third_name = models.CharField(max_length=100, verbose_name="Отчетсво Сотрудника")
    position = models.ForeignKey('Position', on_delete=models.CASCADE, verbose_name="Должность сотрудника", null=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name="Отдел сотрудника", null=True)
    subdivision = models.ForeignKey('Subdivision', on_delete=models.CASCADE, verbose_name="Подразделение")
    date_of_employment = models.DateField(help_text="В формате: 2022-01-17", verbose_name="Дата устройства на работу", null=True, blank=True)

    def __str__(self):
        return str(self.date_of_employment)


