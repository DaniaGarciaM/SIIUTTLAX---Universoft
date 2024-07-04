from django.contrib import admin

# Register your models here.
from .models import Semester,Period

admin.site.register(Semester)
admin.site.register(Period)
