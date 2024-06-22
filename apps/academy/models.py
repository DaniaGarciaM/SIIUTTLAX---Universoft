from django.db import models
from django.contrib.auth.models import User

class Employee(User):
    tipos = [
        ('prof','Docente'),
        ('direc','Director')
    ]
    num_empleado = models.IntegerField()
    tipo = models.CharField(max_length=15, choices=tipos)

    def __str__(self):
        return self.num_empleado
    
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
    
class Student(User):
    matricula = models.CharField(max_length=20)
    def __str__(self):
        return self.matricula
    
    class Meta: #Español
        verbose_name = "Student"
        verbose_name_plural = "Students"
    