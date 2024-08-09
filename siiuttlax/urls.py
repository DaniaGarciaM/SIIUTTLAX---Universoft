from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns = [
    path('', include('apps.home.urls')),
    path('admin/', admin.site.urls),
    path('academy/', include('apps.academy.urls')),
    path('career/', include('apps.career.urls')),
    
    
    path("usuarios/",views.usuarios_view, name="usuarios"),
    path('alumnos/', views.alumnos_view, name='alumnos'),
    path('docentes/', views.docentes_view, name='docentes'),
    path('directores/', views.directores_view, name='directores'),
    path('accounts/', include('django.contrib.auth.urls')),
    

    path('inicio/' ,views.inicio_view, name="inicio"),
    path('semester/', views.semester_view, name='semestre'),
] 
