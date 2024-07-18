from django.urls import path
from . import views

app_name = 'academy'

urlpatterns = [
    path('student/create', 
         views.create_student,
         name='create_student'),
    path('professor_create',
         views.create_professor,
         name='create_professor')
]