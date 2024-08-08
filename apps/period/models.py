from django.db import models

# Create your models here.
class Period(models.Model):
    PERIODS = [
        ('enero - abril', 'enero - abril'),
        ('mayo - agosto', 'mayo - agosto'),
        ('septiembre - diciembre', 'septiembre - diciembre')
    ]
    period = models.CharField(max_length=25, choices=PERIODS)
    year = models.CharField(max_length=4)
    cicle = models.CharField(max_length=11, default='2023-2024')

    def __str__(self):
        return self.period
    
    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"

class Semester(models.Model):
    semester = models.IntegerField(verbose_name="Semestre")
    semester_name = models.CharField(max_length=20, verbose_name="Nombre Semestre")

    def __str__(self):
        return f"{str(self.semester)} °"
    
    class Meta:
        verbose_name = "Semestre"
        verbose_name_plural = "Semestres"