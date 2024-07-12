from django.contrib import admin

# Register your models here.
from .models import Student,Category,Professor

admin.site.register(Student)
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'category', 'employee_number', 'title')
    fields = ('first_name', 'last_name', 'category', 'employee_number', 'title')
admin.register(Student)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'enrollment')
    fields = ('first_name', 'last_name', 'enrollment', 'email')