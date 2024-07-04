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

class Semester(models.Model):
    semester = models.IntegerField()
    semester_name = models.CharField(max_length=20)