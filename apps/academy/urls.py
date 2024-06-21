from django.urls import path
from .views import hello

app_name = 'academy'

urlpatterns = [
    path('', hello),
]