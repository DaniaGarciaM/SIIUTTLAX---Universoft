from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProfessorForm, StudentForm
# Create your views here.
def create_professor(request):
    form = ProfessorForm()
    return render(request,
                  'academy/create_prof.html',
                  {'form': form})

def create_student(request):
    form = StudentForm()
    return render(request,
                  'academy/create_student.html',
                  {'form': form})
    
