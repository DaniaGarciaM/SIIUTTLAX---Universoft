from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(User):
    user_id = models.IntegerField(verbose_name="")
    phone = models.IntegerField(verbose_name="Telefono")
    second_lastname= models.CharField(max_length=150, verbose_name="Segundo apellido")
