# Generated by Django 4.2 on 2024-09-19 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_employee_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(choices=[('Администратор системы', 'Администратор системы'), ('Системный администратор', 'Системный администратор'), ('Контент менеджер аппарата управления', 'Контент менеджер аппарата управления'), ('Редактор', 'Редактор'), ('Пользователь системы', 'Пользователь системы')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]