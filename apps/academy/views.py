from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ProfessorForm, StudentForm
from .models import Professor, Student
# Create your views here.
def create_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password']
            category = form.cleaned_data['category']
            employee_number = form.cleaned_data['employee_number']

            Professor.objects.create(
                username = username,
                first_name = first_name,
                password = password,
                category = category,
                employee_number = employee_number
            )
            return redirect('academy:professors_create')
    form = ProfessorForm()    
    return render(request,
                  'academy/create_professor.html',
                  {'form': form})

def create_student(request):
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password']
            matricula = form.cleaned_data['employee_number']

            Professor.objects.create(
                username = username,
                first_name = first_name,
                password = password,
                matricula = matricula
            )
            return redirect('academy:student_create')
    form = ProfessorForm()    
    form = StudentForm()
    return render(request,
                  'academy/create_student.html',
                  {'form': form})
    
