# Generated by Django 4.0.1 on 2022-01-16 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Отдел')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Должность')),
            ],
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Подразделение')),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя сотрудника')),
                ('second_name', models.CharField(max_length=100, verbose_name='Фамилия сотрудника')),
                ('third_name', models.CharField(max_length=100, verbose_name='Отчетсво Сотрудника')),
                ('date_of_employment', models.DateField(blank=True, null=True, verbose_name='Дата устройства на работу')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.department', verbose_name='Отдел сотрудника')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.position', verbose_name='Должность сотрудника')),
            ],
        ),
    ]
