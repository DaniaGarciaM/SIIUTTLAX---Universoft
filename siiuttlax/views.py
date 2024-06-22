from django.shortcuts import render

def alumnos_view(request):
    context = {
        'alumnos': [
            {'matricula': '20212ITID','nombre': 'Juan', 'carrera': 'IDGS'},
            {'matricula': '20212ITID','nombre': 'Dania', 'carrera': 'IDGS'},
            {'matricula': '20212ITID','nombre': 'Miguel', 'carrera': 'IDGS'},
            {'matricula': '20212ITID','nombre': 'Leonel', 'carrera': 'IDGS'},
        ]
    }
    return render(request, 'alumnos.html', context)

def docentes_view(request):
    context = {
        'docentes': [
            {'nombre': 'Prof. Paco', 'status': 'Activio'},
            {'nombre': 'Prof. Diana', 'status': 'Activo'},
        ]
    }
    return render(request, 'docentes.html', context)

def directores_view(request):
    context = {
        'directores': [
            {'n_empleado':'1','nombre': 'Carlos', 'departamento': 'Administración'},
            {'n_empleado':'2','nombre': 'Laura', 'departamento': 'Recursos Humanos'},
        ]
    }
    return render(request, 'directores.html', context)