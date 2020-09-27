from django import forms
from django.forms import ModelForm
from .models import Klase
#Se requiere modificar este form
class ClaseForm(ModelForm):
	class Meta:
		model = Klase
		fields = ['NombreClas','ClassInicio', 'ClassTermino', 'Profesor', 'AsistHombres', 'AsistMujeres', 'AsistTotales', 'AsistPorcentaje', 'PaseVencidos']