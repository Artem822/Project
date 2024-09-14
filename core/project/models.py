from django.db import models

class Skip(models.Model):
    CHOICE = [
        ('Уважительная', 'Уважительная'),
        ('Не уважительная', 'Не уважительная'),
    ]
    title = models.CharField(max_length=100)
    skip_from = models.DateField()
    skip_to = models.DateField(blank=True, null=False)
    cause = models.CharField(max_length=50, choices=CHOICE)
    
    def __str__(self) -> str:
        return self.title

class Education(models.Model):
    title = models.CharField(max_length=100)
    education_from = models.DateField(blank=True, null=False)
    education_to = models.DateField(blank=True, null=False)
    
    def __str__(self) -> str:
        return self.title
    
class Employee(models.Model):
    CHOICE = [
        ('Администратор системы', "Администратор системы"),
        ('Системный администратор', 'Системный администратор'),
        ('Контент менеджер аппарата управления', 'Контент менеджер аппарата управления'),
        ('Редактор', 'Редактор'),
        ('Пользователь системы', 'Пользователь системы')
    ]
    firts_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='data/')
    work_phone = models.IntegerField()
    email = models.EmailField()
    home_phone = models.IntegerField(blank=True, null=True)
    cabinet = models.IntegerField()
    role = models.CharField(max_length=50, choices=CHOICE)
    skip = models.ManyToManyField(to=Skip, blank=True)
    education = models.ForeignKey(to=Education, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return f"{self.firts_name} {self.middle_name} {self.last_name}" 
    
