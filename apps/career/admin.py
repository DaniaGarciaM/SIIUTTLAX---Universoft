from django.contrib import admin

# Register your models here.
from .models import Career, Subject

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display=('short_name', 'level', 'name')
    ordering = ['level', 'short_name']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'career', 'semester', 'weekly_hours', 'total_hours']
    list_filter = ['career', 'semester']
