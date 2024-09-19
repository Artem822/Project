from django import forms
from .models import Employee, Skip

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['role', 'work_phone', "home_phone", 'education']

class SkipForm(forms.ModelForm):
    class Meta:
        model = Skip
        fields = "__all__"
        