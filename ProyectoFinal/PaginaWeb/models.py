from django.db import models
from django.contrib.auth.models import User


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField ()
    def __str__(self) -> str:

        return(f"Nombre: {self.nombre} - Comision {self.comision}")

class Profesores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self) -> str:

        return(f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profesion: {self.profesion}")

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self) -> str:

        return(f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}")


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_entrega = models.DateField()
    entregado = models.CharField(max_length=2)
    def __str__(self) -> str:

        return(f"Nombre: {self.nombre}")

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.user.username