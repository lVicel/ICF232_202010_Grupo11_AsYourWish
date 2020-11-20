from django import forms
from django.forms import ModelForm
from .models import Profesor
#Se requiere modificar este form
class ProfesorForm(ModelForm):
	class Meta:
		model = Profesor
		fields = [
			'RUTprof', 
			'NombreProf', 
			'GeneroProf', 
			'LocalPerteneciente', 
			'ClaseProfesor', 
			'EmailProf', 
			'NtelefonoProf']
		
		labels = {
			'RUTprof': 'RUT', 
			'NombreProf' : 'Nombre', 
			'GeneroProf': 'Genero', 
			'LocalPerteneciente' : 'Local Perteneciente', 
			'ClaseProfesor' : 'Clase Asignada', 
			'EmailProf' : 'E-amil', 
			'NtelefonoProf' : 'Telefono',
		}

		widgets = {
			'RUTprof' : forms.TextInput(attrs={'class' : 'forms-control'}),
			'NombreProf' : forms.TextInput(attrs={'class' : 'forms-control'}), 
			'GeneroProf': forms.Select(attrs={'class' : 'forms-control'}),
			'LocalPerteneciente' : forms.TextInput(attrs={'class' : 'forms-control'}), 
			'ClaseProfesor' : forms.TextInput(attrs={'class' : 'forms-control'}), 
			'EmailProf': forms.EmailInput(), 
			'NtelefonoProf' : forms.TextInput(attrs={'class' : 'forms-control'}),
		}