from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    user = request.user
    return render(request, 'home/home.html', {'user':user})