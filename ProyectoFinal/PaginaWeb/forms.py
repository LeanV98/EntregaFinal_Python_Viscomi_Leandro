from django import forms
from django.contrib.auth.forms import UserCreationForm , UserModel, UserChangeForm
from django.contrib.auth.models import User 
from django.forms.widgets import DateInput
from django.core.validators import MaxLengthValidator

class CursoForm(forms.Form):
    nombre=forms.CharField(max_length=40)
    comision=forms.IntegerField()

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=40) 
    apellido = forms.CharField(max_length=40) 
    email = forms.EmailField() 
    profesion = forms.CharField(max_length=40) 


class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=40) 
    apellido = forms.CharField(max_length=40) 
    email = forms.EmailField() 
    
class EntregableForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    fecha_entrega = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), input_formats=['%Y-%m-%d'])
    entregado = forms.CharField(max_length=2, validators=[MaxLengthValidator(2)])


class UserCreationFormCustom(UserCreationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput)
    email = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    imagen = forms.ImageField(label="Avatar", required=False)  

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2', 'imagen']  
        help_texts = {k: "" for k in fields}
        

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Correo electrónico")
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre") 
    avatar = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'avatar']
        help_texts = {k: "" for k in fields}