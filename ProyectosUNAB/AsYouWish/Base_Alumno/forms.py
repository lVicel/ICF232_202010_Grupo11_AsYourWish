from django import forms
from django.forms import ModelForm
from .models import Alumno, Participante, ParticipantesEvent, PagosAlumno

#Se requiere modificar este form
class AlumnoForm(ModelForm):
	class Meta:
		model = Alumno
		fields = [
			'RUT',
			'Nombre',
			'Genero',
			'Nacimiento',
			'Profesion',
			'DirPersonal',
			'DirLaboral',
			'Email',
			'Ntelefono',
			]
		
		labels = {
			'RUT' :'RUT',
			'Nombre' : 'Nombre',
			'Genero' : 'Genero',
			'Nacimiento' : 'Fecha Nacimiento',
			'Profesion' : 'Profesion',
			'DirPersonal' : 'Direccion Personal',
			'DirLaboral' : 'Direccion Laboral',
			'Email' : 'E-mail',
			'Ntelefono' : 'Telefono',
		}

		widgets = {
			'RUT' : forms.TextInput(attrs={'class' : 'forms-control'}),
			'Nombre' : forms.TextInput(attrs={'class' : 'forms-control'}),
			'Genero' : forms.Select(attrs={'class' : 'forms-control'}),
			'Nacimiento' : forms.SelectDateWidget(years=range(1950,2101)),
			'Profesion' : forms.TextInput(attrs={'class' : 'forms-control'}),
			'DirPersonal' : forms.TextInput(attrs={'class' : 'forms-control'}),
			'DirLaboral' : forms.TextInput(attrs={'class' : 'forms-control'}),
			'Email' : forms.EmailInput(),
			'Ntelefono' : forms.TextInput(attrs={'class' : 'forms-control'}),
		}




class ParticipanteForm(ModelForm):
	class Meta:
		model = Participante
		fields = [
			'Nombre',
			'Clase_Perteneciente',
			'Local',
			'Horario_Inicio',
			'Horario_Termino',
			'AsistPorcentaje',
			'AsistTotales',
			'Code_Clase',
			]
		
		labels = {
			'Nombre' : 'Nombre',
			'Clase_Perteneciente' : 'Clase a la que Pertenece',
			'Horario_Inicio' : 'Horario Inicio Clase',
			'Horario_Termino' : 'Horario Termino Clase',
			'AsistTotales' : 'Asistencias Totales',
			'Code_Clase' : 'ID de la Clase',
		}

		widgets = {
			'Nombre' : forms.TextInput(attrs={'class' : 'forms-control'}),
			'Clase_Perteneciente' : forms.TextInput(attrs={'class' : 'forms-control'}),
		}

class ParticipanteEventForm(ModelForm):
	class Meta:
		model = ParticipantesEvent
		fields= [
			'EventInscrito',
			'ID_Event',
    		'NombreParticipante',
    		'Escena',
		]

		labels= {
			'EventInscrito' : 'Evento Inscrito',
    		'NombreParticipante' : 'Nombre Participante',
    		'Escena' : 'Escena participante',
		}

		widgets={
			'EventInscrito' : forms.TextInput(attrs={'class' : 'forms-control'}),
    		'NombreParticipante' : forms.TextInput(attrs={'class' : 'forms-control'}),
    		'Escena' : forms.TextInput(attrs={'class' : 'forms-control'}),
		}

class PagosForm(ModelForm):
	class Meta:
		model = PagosAlumno
		fields= [
			'id_Alumno',
			'RUT',
    		'Nombre',
			#'FechaIngresos',
			'Local',
    		'ClasePagada',
			'Horario_Inicio',
    		'Horario_Termino',
			'IngresoAlumnno',
			'MetodoPago',
		]

		labels= {
			'RUT' : 'RUT',
    		'Nombre' : 'Nombre',
			#'FechaIngresos'
			'Local' : 'Local',
    		'ClasePagada' : 'Nombre de la Clase',
			'Horario_Inicio':'Horario Inicio',
    		'Horario_Termino':'Horario Termino',
			'IngresoAlumnno' : 'Ingreso',
			'MetodoPago' :'Metodo de Pago',
		}

		widgets={
			'RUT' : forms.TextInput(attrs={'class' : 'forms-control'}),
    		'Nombre' : forms.TextInput(attrs={'class' : 'forms-control'}),
			#'FechaIngresos'
			'Local' : forms.TextInput(attrs={'class' : 'forms-control'}),
    		'ClasePagada' : forms.TextInput(attrs={'class' : 'forms-control'}),
			'Horario_Inicio': forms.TextInput(attrs={'class' : 'forms-control'}),
    		'Horario_Termino': forms.TextInput(attrs={'class' : 'forms-control'}),
			'IngresoAlumnno' : forms.NumberInput(),
			'MetodoPago' : forms.TextInput(attrs={'class' : 'forms-control'}),
		}