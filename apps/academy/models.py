from django.db import models
from django.contrib.auth.models import User

class Professor(User):
    no_empleado = models.IntegerField()
    puesto_id = models.IntegerField()
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.no_empleado
    
    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professors"

class Category(models.Model):
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=15)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Student(User):
    matricula = models.CharField(max_length=20)
    def __str__(self):
        return self.matricula
    
    class Meta: 
        verbose_name = "Student"
        verbose_name_plural = "Students"
    