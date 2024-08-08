from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=150, verbose_name="Categoría")
    short_name = models.CharField(max_length=15, verbose_name="Abreviatura")
    description = models.TextField(verbose_name="Descripción")
    
    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = "Categoría Profesor"
        verbose_name_plural = "Categorías Profesores"

class Professor(User):
    title = models.CharField(max_length=50, verbose_name="Título")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True, blank=True, verbose_name="Categoría"
    )
    employee_number = models.CharField(max_length=5, verbose_name="No. Empleado", default="0000")
    
    def __str__(self):
        return self.employee_number
    
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

class Student(User):
    
    matricula = models.CharField(max_length=20, verbose_name="Matrícula")
    def __str__(self):
        return f"{self.matricula} | {self.first_name} {self.last_name}"
    
    class Meta: 
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
    