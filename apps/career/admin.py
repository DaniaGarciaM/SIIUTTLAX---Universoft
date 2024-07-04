from django.contrib import admin

# Register your models here.
from .models import Career, Subject

admin.site.register(Career)
admin.site.register(Subject)
