from django import forms
from django.forms import ModelForm
from .models import Evento
#Se requiere modificar este form
class EventoForm(ModelForm):
	class Meta:
		model = Evento
		fields = ['NombreEvent', 'FechaEvent', 'EventInicio', 'EventTermino', 'LocalAdmin', 'Direccion']