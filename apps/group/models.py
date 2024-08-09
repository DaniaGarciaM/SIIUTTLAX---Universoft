from django.db import models
from apps.period.models import Semester
from apps.period.models import Period
from apps.career.models import Career
from apps.academy.models import Professor
from apps.career.models import Subject
from apps.academy.models import Student

class Group (models.Model):
    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Semestre"
    )
    group = models.CharField(max_length=1, verbose_name="Grupo")
    observations = models.CharField(max_length=100, verbose_name="Observaciones")
    period = models.ForeignKey(
        Period,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Periodo"
    )
    subjects = models.ManyToManyField(Subject, verbose_name="Materias")
    career = models.ForeignKey(
        Career,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Carrera"
    )
    tutor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Tutor"
    )
    students = models.ManyToManyField(
        Student,
        verbose_name="Estudiantes"
        
    )

    def __str__(self):
        return f"{str(self.semester)} {self.group} | {self.career}"

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
    

class Group_Subject(models.Model):
    group_id = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Grupo"
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Materia"
    )
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Profesor"
    )

    class Meta:
        verbose_name = "Grupo-Materia"
        verbose_name_plural = "Grupo-Materias"

    def __str__(self):
        return f"{str(self.subject)} {self.group_id}"

class Group_Student(models.Model):
    group= models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Grupo"
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Estudiante"
    )

    def __str__(self):
        return str(self.group)
    
    class Meta:
        verbose_name = "Grupo-Estudiante"
        verbose_name_plural = "Grupo-Estudiantes"   