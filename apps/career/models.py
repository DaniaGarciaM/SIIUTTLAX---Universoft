from django.db import models
from apps.academy.models import Professor
from apps.period.models import semester

# Create your models here.
class Career (models.Model):
    name = models.CharField(max_length=100, verbose_name="Carrera")

    director = models.ForeignKey(
         Professor,
         on_delete=models.CASCADE,
         null=True,
         blank=True,
         verbose_name="Director"
    )
    levels = [
        ('TSU','Técnico Superior Universitario'),
        ('ING', 'Ingenieria'),
        ('MTR', 'Maestria'),
        ('Lic', 'Licenciatura')

    ]
    level = models.CharField(max_length=5, choices=levels, verbose_name="Nivel de estudios")
    
    short_name = models.CharField(max_length=10, verbose_name="Abreviatura")


    status = models.BooleanField(True, verbose_name="Status")

    year_plan =  models.CharField(max_length=4, verbose_name="Año")

    
    
    def __str__(self):
        return self.short_name
    
    class Meta:
        verbose_name = "Career"
        verbose_name_plural = "Careers"
    
class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Materia")
    career = models.ForeignKey(Career, on_delete=models.CASCADE, verbose_name="Carrera")
    semester = models.ForeignKey(
        semester,
        on_delete=models.CASCADE,
        default=1,
        verbose_name="Semestre"

    )
    total_hours = models.IntegerField(verbose_name="Horas totales")
    weekly_hours = models.IntegerField(verbose_name="Horas semanales")
    file = models.CharField(max_length=100, verbose_name="Hoja de asignatura")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"