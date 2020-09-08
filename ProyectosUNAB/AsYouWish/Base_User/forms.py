from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
				'username',
				'id',
				'email',
			]
		labels = {
				'username': 'Nombre de usuario',
				'id': 'Rut',
				'email': 'Correo',
		}
