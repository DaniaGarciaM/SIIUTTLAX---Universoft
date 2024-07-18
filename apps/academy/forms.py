from django import forms
from .models import Professor, Student

class ProfessorForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields= ['username', 'password', 'first_name', 'employee_number', 'category']
        widgets = {
            'password': forms.PasswordInput(),
            'employee_number': forms.NumberInput(),
            'category': forms.Select()
        }

class StudentForm(forms.ModelForm):

    class Meta:
        model= Student
        fields = ['username', 'password', 'first_name', 'matricula']
        widgets = {
            'password': forms.PasswordInput(),
            
        }
