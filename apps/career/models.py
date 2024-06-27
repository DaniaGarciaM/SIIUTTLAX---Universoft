from django.db import models

# Create your models here.
class Career (models.Model):
    name = models.CharField(max_length=100)
    levels = [
        ('TSU','Técnico Superior Universitario'),
        ('ING', 'Ingenieria'),
        ('MTR', 'Maestria'),
        ('Lic', 'Licenciatura')

    ]
    level = models.CharField(max_length=5, choices=levels)
    
    short_name = models.CharField(max_length=10)


    status = models.BooleanField(True)

    year_plan =  models.CharField(max_length=4)

    
    
    def __str__(self):
        return self.short_name
    
    class Meta:
        verbose_name = "Career"
        verbose_name_plural = "Careers"
    
class Subject(models.Model):
    name = models.CharField(max_length=100)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    semester = models.IntegerField()
    total_hours = models.IntegerField()
    weekly_hours = models.IntegerField()
    file = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"