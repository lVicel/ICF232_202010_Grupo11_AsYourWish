from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
