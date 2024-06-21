from django.urls import path
from .views import career


app_name = 'career'

urlpatterns = [
    path('', career)
]
