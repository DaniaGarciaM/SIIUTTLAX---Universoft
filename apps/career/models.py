from django.db import models

# Create your models here.
class Career (models.Model):
    names = models.CharField(max_length=75)

    levels = [
        ('TSU','Técnico Superior Universitario'),
        ('ING', 'Ingenieria'),
        ('MTR', 'Maestria'),
        ('Lic', 'Licenciatura')

    ]
    level = models.CharField(max_length=5, choices=levels)

    short_names = [
        #TSU
        ('TIADSM', 'TIADSM'),
        ('IDGS', 'IDGS'),
        ('DNAM', 'DNAM'),
        ('AACH', 'AACH'),
        ('MAI', 'MAI'),
        ('TIAIR', 'TIAIR'),
        ('TIAEVND', 'TIAEVND'),
        ('PIAP', 'PIAP'),
        ('PIAM', 'PIAM'),
        ('PIAA', 'PIAA'),
        ('MAA', 'MAA'),
        ('MAR', 'MAR'),
        ('DMIAP', 'DMIAP'),
        #LICENCIATURAS
        ('INM', 'INM'),
        ('GCH', 'GCH'),
        #INGENIERÍA
        ('IRIC', 'IRIC'),
        ('IEVND', 'IEVND'),
        ('IT', 'IT'),
        ('IDGS', 'IDGS'),
        ('IPOI', 'IPOI'),
        ('IMI', 'IMI'),
        ('IDTM', 'IDTM'),
        #POSGRADO
        ('IGP', 'IGP')
    ]
    
    
    short_name = models.CharField(max_length=10)


    status_activo = models.BooleanField(True)
    status_inactivo = models.BooleanField(False)

    plan =  models.DateField()
    
    
    def __str__(self):
        return self.short_name
    