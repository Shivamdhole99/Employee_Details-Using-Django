from django import forms
from .models import employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['name', 'email', 'department', 'salary']
