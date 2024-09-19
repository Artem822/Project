from django import forms
from .models import Employee, Skip, Education
from django.contrib.auth import forms as f
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['role', 'work_phone', "home_phone", 'education']

class SkipForm(forms.ModelForm):
    class Meta:
        model = Skip
        fields = "__all__"

class UserForm(f.UserCreationForm):
    class Meta:
        model = Employee
        fields = ['username', 'photo', 'password1', 'password2','role', 'email', 'education']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = "__all__"