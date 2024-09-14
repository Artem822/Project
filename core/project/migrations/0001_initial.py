# Generated by Django 4.2 on 2024-09-14 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('education_from', models.DateField(blank=True)),
                ('education_to', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('skip_from', models.DateField()),
                ('skip_to', models.DateField(blank=True)),
                ('cause', models.CharField(choices=[('Уважительная', 'Уважительная'), ('Не уважительная', 'Не уважительная')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firts_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='data/')),
                ('work_phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('home_phone', models.IntegerField(blank=True, null=True)),
                ('cabinet', models.IntegerField()),
                ('role', models.CharField(choices=[('Администратор системы', 'Администратор системы'), ('Системный администратор', 'Системный администратор'), ('Контент менеджер аппарата управления', 'Контент менеджер аппарата управления'), ('Редактор', 'Редактор'), ('Пользователь системы', 'Пользователь системы')], max_length=50)),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='project.education')),
                ('skip', models.ManyToManyField(blank=True, to='project.skip')),
            ],
        ),
    ]