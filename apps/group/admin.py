from django.contrib import admin

# Register your models here.
from .models import Group, Group_Student, Group_Subject
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display=('career', 'semester', 'group', 'period', 'tutor')
@admin.register(Group_Subject)
class Group_SubjectAdmin(admin.ModelAdmin):
    list_display=('subject', 'group_id', 'professor')
admin.site.register(Group_Student)
