from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required

def usuarios_view(request):
    return render(request, 'users/usuarios.html')

def alumnos_view(request):
    context = {
        'alumnos': [
            {'matricula': '20212ITID','nombre': 'Juan', 'carrera': 'IDGS'},
            {'matricula': '20212ITID','nombre': 'Dania', 'carrera': 'IDGS'},
            {'matricula': '20212ITID','nombre': 'Miguel', 'carrera': 'IDGS'},
            {'matricula': '20212ITID','nombre': 'Leonel', 'carrera': 'IDGS'},
        ]
    }
    return render(request, 'users/alumnos.html', context)

def docentes_view(request):
    context = {
        'docentes': [
            {'nombre': 'Prof. Paco', 'status': 'Activio'},
            {'nombre': 'Prof. Diana', 'status': 'Activo'},
        ]
    }
    return render(request, 'users/docentes.html', context)

def directores_view(request):
    context = {
        'directores': [
            {'n_empleado':'1','nombre': 'Carlos', 'departamento': 'Administración'},
            {'n_empleado':'2','nombre': 'Laura', 'departamento': 'Recursos Humanos'},
        ]
    }
    return render(request, 'users/directores.html', context)


@login_required
def semester_view(request):
    context = {
        'semestre':[
            {'n_empleado':'2','nombre': 'Laura', 'departamento': 'Recursos Humanos'},
        ]
    }
    return render(request, 'semester/inicio.html', context)

def inicio_view(request):
    context = {
        'group':[
        {'semester_id': 1, 'semester': 1, 'semester_name': 'Primer Cuatrimestre'},
        {'semester_id': 2, 'semester': 2, 'semester_name': 'Segundo Cuatrimestre'},
        {'semester_id': 3, 'semester': 3, 'semester_name': 'Tercer Cuatrimestre'},
        ]
    }
    
    return render(request, 'semester/inicio.html', context)