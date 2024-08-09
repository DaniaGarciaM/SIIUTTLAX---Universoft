from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ProfessorForm, StudentForm
from .models import Professor, Student
from django.contrib import messages
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

            

            Professor.objects.create_user(
                username = username,
                first_name = first_name,
                password = password,
                category = category,
                employee_number = employee_number
            )
            # messages.add_message(request,'Se a creado con exito!')
            return redirect('home:home')
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
            matricula = form.cleaned_data['matricula']

            Student.objects.create_user(
                username = username,
                first_name = first_name,
                password = password,
                matricula = matricula
            )
            # return redirect('academy:create_student')
            return redirect('home:home')
    form = ProfessorForm()    
    form = StudentForm()
    return render(request,
                  'academy/create_student.html',
                  {'form': form})
    
