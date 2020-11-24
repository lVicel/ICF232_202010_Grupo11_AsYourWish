from django import forms
from django.forms import ModelForm
from .models import Klase
#Se requiere modificar este form
class ClaseForm(ModelForm):
	class Meta:
		model = Klase
		fields = [
		'NombreClas',
		'Local',
		'Dia',
		'ClassInicio', 
		'ClassTermino',
		'Profesor',
		]


		labels={
			'NombreClas' : 'Nombre de la Clase',
			'Local': 'Local',
			'Dia':'Dia Semana',
			'ClassInicio' : 'Hora Inicio',
			'ClassTermino': 'Hora Termino',
			'Profesor' : 'Profesor Jefe',
		}

		widgets = {
			'Profesor' : forms.TextInput(attrs={'class' : 'forms-control','placeholder': 'Primer Nombre & Apellidos'}),
			'ClassInicio' : forms.TextInput(attrs={'class' : 'forms-control','placeholder': 'Formato de 24 Horas'}),
			'ClassTermino' : forms.TextInput(attrs={'class' : 'forms-control','placeholder': 'Formato de 24 Horas'}),
			'Local': forms.Select(attrs={'class' : 'forms-control'}),
			'Dia' : forms.Select(attrs={'class' : 'forms-control'}),
		}