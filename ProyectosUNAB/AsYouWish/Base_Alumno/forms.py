from django import forms
from django.forms import ModelForm
from .models import Alumno
#Se requiere modificar este form
class AlumnoForm(ModelForm):
	class Meta:
		model = Alumno
		fields = ['RUT', 'Nombre', 'Nacimiento', 'Profesion', 'DirPersonal', 'DirLaboral', 'Asistencias']