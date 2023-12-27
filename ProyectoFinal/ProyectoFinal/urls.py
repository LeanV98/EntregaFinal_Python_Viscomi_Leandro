"""
URL configuration for Pagina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PaginaWeb import views
from django.contrib.auth.views import LogoutView,LoginView
from PaginaWeb.views import CambiarContrasenia
from django.conf import settings
from django.conf.urls.static import static
from PaginaWeb.views import login_request, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="Inicio"),
    path('bienvenida/', views.bienvenida, name="Bienvenida"),
    #path('cursos/', views.cursos, name="Cursos"),
    #path('profesores/', views.profesores, name="Profesores"),
    #path('estudiantes/', views.estudiantes, name="Estudiantes"),
    #path('entregables/', views.entregables, name="Entregables"),
    path('about/', views.acerca_de_mi, name='AcercaDeMi'),
    path('leermas/', views.leer_mas, name='LeerMas'),


    path('cursos/lista', views.CursoListView.as_view(), name="ListaCurso"),
    path('cursos/nuevo', views.CursoCreateView.as_view(), name="NuevoCurso"),
    path('cursos/<pk>', views.CursoDetailView.as_view(), name="DetalleCurso"),
    path('cursos/<pk>/editar', views.CursoUpdateView.as_view(), name="EditarCurso"),
    path('cursos/<pk>/borrar', views.CursoDeleteView.as_view(), name="BorrarCurso"),


    path('estudiantes/lista', views.EstudiantesListView.as_view(), name="ListaEstudiante"),
    path('estudiantes/nuevo', views.EstudiantesCreateView.as_view(), name="NuevoEstudiante"),
    path('estudiantes/<pk>', views.EstudiantesDetailView.as_view(), name="DetalleEstudiante"),
    path('estudiantes/<pk>/editar', views.EstudiantesUpdateView.as_view(), name="EditarEstudiante"),
    path('estudiantes/<pk>/borrar', views.EstudiantesDeleteView.as_view(), name="BorrarEstudiante"),

    path('profesores/lista', views.ProfesorListView.as_view(), name="ListaProfesor"),
    path('profesores/nuevo', views.ProfesorCreateView.as_view(), name="NuevoProfesor"),
    path('profesores/<pk>', views.ProfesorDetailView.as_view(), name="DetalleProfesor"),
    path('profesores/<pk>/editar', views.ProfesorUpdateView.as_view(), name="EditarProfesor"),
    path('profesores/<pk>/borrar', views.ProfesorDeleteView.as_view(), name="BorrarProfesor"),

    path('entregables/lista', views.EntregableListView.as_view(), name="ListaEntregable"),
    path('entregables/nuevo', views.EntregableCreateView.as_view(), name="NuevoEntregable"),
    path('entregables/<pk>', views.EntregableDetailView.as_view(), name="DetalleEntregable"),
    path('entregables/<pk>/editar', views.EntregableUpdateView.as_view(), name="EditarEntregable"),
    path('entregables/<pk>/borrar', views.EntregableDeleteView.as_view(), name="BorrarEntregable"),


    path('login/', login_request, name='Login'),
 
    path('registro/', views.registro, name="Registro"), 
    path('logout/', logout_view, name='logout'),
    path('editar_perfil/', views.editarPerfil, name="EditarPerfil"),
    path('cambiar_contrasenia/', views.CambiarContrasenia.as_view(), name="CambiarContrasenia"),
    
]
    


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)