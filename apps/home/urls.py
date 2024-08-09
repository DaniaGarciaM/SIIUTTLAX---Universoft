from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.student, name='student'),
    path('professor/', views.professor, name='professor'),
]
