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
		'ClassInicio', 
		'ClassTermino',
		'Profesor', 
		'AsistHombres', 
		'AsistMujeres', 
		'AsistTotales', 
		'AsistPorcentaje', 
		'PaseVencidos']


		labels={
			'NombreClas' : 'Nombre de la Clase',
			'Local': 'Local',
			'ClassInicio' : 'Hora Inicio',
			'ClassTermino': 'Hora Termino',
			'Profesor' : 'Profesor Jefe',
		}
  
DISPLAY_CHOICES = (
	("participante", "Display participante")
)