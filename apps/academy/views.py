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
            form.save()
            return redirect('academy/create_professor')
        
    form = ProfessorForm() 
    return render(request,
                  'academy/create_professor.html',
                  {'form': form})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('academy/create_student')
        
    form = ProfessorForm()    
    form = StudentForm()
    return render(request, 'academy/create_student.html', {'form': form})
    
