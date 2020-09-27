from django import forms
from django.forms import ModelForm
from .models import Profesor
#Se requiere modificar este form
class ProfesorForm(ModelForm):
	class Meta:
		model = Profesor
		fields = ['RUTprof', 'NombreProf', 'GeneroProf', 'LocalPerteneciente', 'ClaseProfesor', 'EmailProf', 'NtelefonoProf']