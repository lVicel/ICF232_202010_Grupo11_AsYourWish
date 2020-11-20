from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django import forms
from .choices import *

class UsuarioForm(UserCreationForm):
	username = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	rut = forms.CharField(max_length=12, required=False, help_text='Optional.')
	residencia = forms.ChoiceField(choices=LUGARES)
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'rut',
			'residencia',
		]
		labels = {
			'username': 'Nombre de usuario',
			'rut': 'Rut',
			'email': 'Correo',
			'residencia': 'Residencia',
		}

# Los 3 Usuarios o Grupos eran los Siguientes:
# Basico --> Solo podra ser capaz de registrar las Asistencias de Alumnos
#
# Anfitrion-->Solo podra visualizar los Datos de las Tablas, pero NO capaz de Registrar, Modificar o Eliminar algun tipo de Objeto o Dato
#
# Director-->Ademas de visualizar los Datos de las Tablas, este tambien podra registrar, Modifcar, o Eliminar algun tipo de Objeto o Dato.
