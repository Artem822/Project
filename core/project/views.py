from typing import Any
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .serizalizers import *
from .models import *
from .forms import *
from rest_framework import viewsets
from django.contrib import messages

class HomeView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['admin_sys'] = Employee.objects.filter(role='Администратор системы')
        context['sys_admin'] = Employee.objects.filter(role='Системный администратор')

        return context
    

class HomeUsersView(TemplateView):
    def get(self,request, id):

        role = {
            0: 'Администратор системы',
            1: 'Системный администратор',
            2: 'Контент менеджер аппарата управления',
            3: 'Редактор',
            4: 'Пользователь системы'
        }[id]

        context = {
            'users': Employee.objects.filter(role=role),
            'title': role,
        }

        return render(request=request, template_name='base.html', context=context)
    

def EditEmployee(request, id):
    Employees = Employee.objects.get(id=id)
    if request.method == 'POST':  
        user_form = EmployeeForm(request.POST,instance=Employees)
        skip_form = SkipForm(request.POST) 
        if user_form.is_valid():
            user_form.save()
            return redirect('home')
        elif skip_form.is_valid():
            skip_form.save()
            Employees.skip.add(skip_form.save())
            return redirect('home')    
    else:
        user_form = EmployeeForm( instance=Employees)
        skip_form = SkipForm()
        
    skips = Employees.skip.all()
    
    return render(request,
                'edit.html',
                {'form': user_form,
                 'employee' : Employees,
                 'skips':skips,
                 'SkipForm':skip_form
                 })

class Panel(TemplateView):
    template_name = 'panel.html'
    def get(self, request):
        user_form = UserForm()
        education_form =EducationForm()
        return render(request, self.template_name, {'UserForm':user_form,
                                                    'EducationForm':education_form})
    
    def post(self,request):
        user_form = UserForm(request.POST, request.FILES)
        education_form =EducationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Пользователь был успешно добавлен")
            return redirect('panel')
        elif education_form.is_valid():
            education_form.save()
            messages.success(request, "Обучение был успешно добавлено")
            return redirect('panel')
        return render(request, self.template_name, {'UserForm':user_form,
                                                    'EducationForm':education_form})

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerizalizer

class EducationViewset(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerizalizer

class SkipViewset(viewsets.ModelViewSet):
    queryset = Skip.objects.all()
    serializer_class = SkipSerizalizer
