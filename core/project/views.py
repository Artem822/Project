from typing import Any
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .serizalizers import *
from .models import *
from .forms import *
from rest_framework import viewsets

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
        form = EmployeeForm(request.POST, instance=Employees)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm(instance=Employees)
    skips = Employees.skip.all()

    return render(request,
                'edit.html',
                {'form': form,
                 'employee' : Employees,
                 'skips':skips})
    
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerizalizer

class EducationViewset(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerizalizer

class SkipViewset(viewsets.ModelViewSet):
    queryset = Skip.objects.all()
    serializer_class = SkipSerizalizer
