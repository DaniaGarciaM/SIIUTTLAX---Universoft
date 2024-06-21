from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def career(request):
    return HttpResponse('<H1>Bienvenido a la vista de carrera<H1>')