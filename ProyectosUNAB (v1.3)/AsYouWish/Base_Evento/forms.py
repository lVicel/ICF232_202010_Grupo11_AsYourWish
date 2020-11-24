from django import forms
from django.forms import ModelForm
from .models import Evento
#Se requiere modificar este form
class EventoForm(ModelForm):
	class Meta:
		model = Evento
		fields = [
		'NombreEvent', 
		'FechaEvent', 
		'EventInicio', 
		'EventTermino', 
		'LocalAdmin', 
		'Direccion',
		]

		labels={
			'NombreEvent' : 'Nombre Evento', 
			'FechaEvent' : 'Fecha', 
			'EventInicio' : 'Horario Inicio', 
			'EventTermino' : 'Horario Termino', 
			'LocalAdmin' : 'Local Encargado', 
			'Direccion' : 'Direccion',
		}

		widgets={
			'NombreEvent' : forms.TextInput(attrs={'class' : 'forms-control'}),
			'FechaEvent' : forms.SelectDateWidget(),
			'EventInicio'  : forms.TextInput(attrs={'class' : 'forms-control','placeholder': 'Formato de 24 Horas'}),
			'EventTermino' : forms.TextInput(attrs={'class' : 'forms-control','placeholder': 'Formato de 24 Horas'}),
			'LocalAdmin' : forms.Select(attrs={'class' : 'forms-control'}),
			'Direccion' : forms.TextInput(attrs={'class' : 'forms-control'}),
		}