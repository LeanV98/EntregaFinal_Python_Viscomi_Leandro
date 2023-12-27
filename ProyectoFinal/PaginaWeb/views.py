from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from PaginaWeb.forms import  UserCreationFormCustom, UserEditForm  
from PaginaWeb.models import Curso,Profesores,Estudiantes,Entregable
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from PaginaWeb.models import Avatar
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


import datetime



def inicio(request):
    return render(request, "otros/index.html")

@login_required(login_url='Inicio') 
def acerca_de_mi(request):
    return render(request, 'otros/about.html')

@login_required(login_url='Inicio') 
def leer_mas(request):
    return render(request, 'otros/leermas.html')

def logout_view(request):
    logout(request)
    return render(request,'otros/index.html')


@login_required(login_url='Inicio')  
def bienvenida(request):
    avatar_url = None

    if hasattr(request.user, 'avatar') and request.user.avatar and request.user.avatar.imagen:
        avatar_url = request.user.avatar.imagen.url

    mensaje_bienvenida = f"Bienvenido, {request.user.username}."
    return render(request, 'otros/bienvenida.html', {'avatar_url': avatar_url, 'mensaje_bienvenida': mensaje_bienvenida})



def login_request(request):
    if request.user.is_authenticated:
        return redirect('Bienvenida')  # Si el usuario ya está autenticado, redirige a la bienvenida

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return redirect('Bienvenida')

            else:
                messages.error(request, "Credenciales incorrectas. Inténtalo de nuevo.")
    else:
        form = AuthenticationForm()

    return render(request, "usuario/login.html", {"form": form})
    

def registro(request):
    if request.user.is_authenticated:
        return redirect('Bienvenida')  # Si el usuario ya está autenticado, redirige a la bienvenida

    if request.method == 'POST':
        form = UserCreationFormCustom(request.POST, request.FILES)

        if form.is_valid():
            usuario = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            imagen = request.FILES.get('imagen')

            nuevo_usuario = form.save(commit=False)
            nuevo_usuario.username = usuario
            nuevo_usuario.email = email
            nuevo_usuario.set_password(password)
            nuevo_usuario.save()

            # Inicia sesión después del registro
            login(request, nuevo_usuario)

            # Verifica si hay una imagen antes de intentar actualizarla
            if imagen:
                avatar, created = Avatar.objects.get_or_create(user=nuevo_usuario)
                avatar.imagen = imagen
                avatar.save()

            return redirect('Bienvenida')

    else:
        form = UserCreationFormCustom()

    return render(request, "usuario/registro.html", {"form": form})

@login_required(login_url='Inicio') 
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user)

        if miFormulario.is_valid():
            # Guarda el formulario sin actualizar la imagen del avatar
            miFormulario.save()

            # Verifica si el usuario tiene un avatar
            if hasattr(usuario, 'avatar'):
                # Ahora, verifica si hay una imagen nueva antes de intentar actualizarla
                if 'avatar' in request.FILES:
                    usuario.avatar.imagen = request.FILES.get('avatar')
                    usuario.avatar.save()
            else:
                # Si el usuario no tiene un avatar, crea uno y guarda la imagen
                avatar = Avatar.objects.create(user=usuario, imagen=request.FILES.get('avatar'))

            messages.success(request, "Perfil actualizado exitosamente.")
            return redirect('Bienvenida')

    else:
        miFormulario = UserEditForm(instance=request.user)

    return render(request, 'usuario/editar_perfil.html', {"miFormulario": miFormulario, "usuario": usuario})
    
@method_decorator(login_required(login_url='Inicio'), name='dispatch')    
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name= 'usuario/cambiar_contrasenia.html'
    success_url = reverse_lazy('EditarPerfil')


@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class EstudiantesListView (ListView):
    model = Estudiantes
    context_object_name = "estudiantes"
    template_name = "estudiantes/estudiantes_listas.html"

@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class EstudiantesDetailView(DetailView):
    model = Estudiantes
    template_name = "estudiantes/estudiantes_detail.html"


@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class EstudiantesCreateView(CreateView):
    model = Estudiantes
    template_name = "estudiantes/estudiantes_crear.html"
    success_url = reverse_lazy('ListaEstudiante')
    fields=['nombre','apellido', 'email']

@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class EstudiantesUpdateView(UpdateView):
    model = Estudiantes
    template_name = "estudiantes/estudiantes_editar.html"
    success_url = reverse_lazy('ListaEstudiante')
    fields=['nombre','apellido', 'email']

@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class EstudiantesDeleteView(DeleteView):
    model = Estudiantes
    template_name = "estudiantes/estudiantes_borrar.html"
    success_url = reverse_lazy('ListaEstudiante')


@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class ProfesorListView (ListView):
    model = Profesores
    context_object_name = "profesores"
    template_name = "profesores/profesores_listas.html"

   
@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class ProfesorDetailView(DetailView):
    model = Profesores
    template_name = "profesores/profesores_detail.html"

@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class ProfesorCreateView(CreateView):
    model = Profesores
    template_name = "profesores/profesores_crear.html"
    success_url = reverse_lazy('ListaProfesor')
    fields=['nombre','apellido', 'email', 'profesion']


@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class ProfesorUpdateView(UpdateView):
    model = Profesores
    template_name = "profesores/profesores_editar.html"
    success_url = reverse_lazy('ListaProfesor')
    fields=['nombre','apellido', 'email', 'profesion']


@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class ProfesorDeleteView(DeleteView):
    model = Profesores
    template_name = "profesores/profesores_borrar.html"
    success_url = reverse_lazy('ListaProfesor')


@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class EntregableListView (ListView):
    model = Entregable
    context_object_name = "entregable"
    template_name = "entregables/entregables_listas.html"


@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class EntregableDetailView(DetailView):
    model = Entregable
    template_name = "entregables/entregables_detail.html"



@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class EntregableCreateView(CreateView):
    model = Entregable
    template_name = "entregables/entregables_crear.html"
    success_url = reverse_lazy('ListaEntregable')
    fields=['nombre','fecha_entrega', 'entregado']


@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class EntregableUpdateView(UpdateView):
    model = Entregable
    template_name = "entregables/entregables_editar.html"
    success_url = reverse_lazy('ListaEntregable')
    fields = ['nombre', 'fecha_entrega', 'entregado']


@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class EntregableDeleteView(DeleteView):
    model = Entregable
    template_name = "entregables/entregables_borrar.html"
    success_url = reverse_lazy('ListaEntregable')


@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class CursoListView (ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "cursos/cursos_listas.html"


@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class CursoDetailView(DetailView):
    model = Curso
    template_name = "cursos/cursos_detail.html"

@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class CursoCreateView(CreateView):
    model = Curso
    template_name = "cursos/cursos_crear.html"
    success_url = reverse_lazy('ListaCurso')
    fields=['nombre','comision']

@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "cursos/cursos_editar.html"
    success_url = reverse_lazy('ListaCurso')
    fields=['nombre','comision']

@method_decorator(login_required(login_url='Inicio'), name='dispatch')
class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "cursos/cursos_borrar.html"
    success_url = reverse_lazy('ListaCurso')
