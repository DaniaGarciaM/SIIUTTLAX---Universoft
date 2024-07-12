from django.contrib import admin

# Register your models here.
from .models import Group, Group_Student, Group_Subject
admin.site.register(Group)
admin.site.register(Group_Subject)
admin.site.register(Group_Student)