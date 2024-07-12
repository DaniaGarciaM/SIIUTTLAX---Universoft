from django.db import models
from apps.period.models import Semester
from apps.period.models import Period
from apps.career.models import Career
from apps.academy.models import Professor
from apps.career.models import Subject
from apps.academy.models import Student

class Group (models.Model):
    semester_id = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Semestre"
    )
    group = models.CharField(max_length=1, verbose_name="Grupo")
    observations = models.CharField(max_length=100, verbose_name="Observaciones")
    period_id = models.ForeignKey(
        Period,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Periodo"
    )
    career_id = models.ForeignKey(
        Career,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Carrera"
    )
    tutor_id = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Tutor"
    )

class Group_Subject(models.Model):
    group_id = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Grupo"
    )
    subject_id = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Materia"
    )
    professor_id = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Profesor"
    )

class Group_Student(models.Model):
    group_id = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Grupo"
    )
    student_id = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Estudiante"
    )
    