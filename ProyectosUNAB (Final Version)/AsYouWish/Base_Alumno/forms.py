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
			'RUT' : forms.TextInput(attrs={'class' : 'forms-control','placeholder': 'Con Punto & Guion'}),
			'Nombre' : forms.TextInput(attrs={'class' : 'forms-control','placeholder': 'Primer Nombre & Apellidos'}),
			'Genero' : forms.Select(attrs={'class' : 'forms-control'}),
			'Nacimiento' : forms.SelectDateWidget(years=range(1950,2101)),
			'Profesion' : forms.TextInput(attrs={'class' : 'forms-control'}),
			'DirPersonal' : forms.TextInput(attrs={'class' : 'forms-control'}),
			'DirLaboral' : forms.TextInput(attrs={'class' : 'forms-control'}),
			'Email' : forms.EmailInput(),
			'Ntelefono' : forms.TextInput(attrs={'class' : 'forms-control'}),
		}

class PagosForm(ModelForm):
	class Meta:
		model = PagosAlumno
		fields= [
    		'id_Alumno',
    		'RUT',
    		'Nombre',
    		'Local',
    		'ClasePagada',
    		'Num_Clases_Pagadas',
    		'Mes',
    		'Anno',
    		'IngresoAlumno',
    		'MetodoPago',
    		'Grupal',
		]

		labels= {
			'id_Alumno':'ID',
    		'RUT':'RUT',
    		'Nombre':'Nombre',
    		'Local':'Local',
    		'ClasePagada':'Clase Pagada',
    		'Num_Clases_Pagadas':'N°Clases Pagadas',
    		'Mes':'Mes',
    		'Anno':'Año',
    		'IngresoAlumno':'Ingreso',
    		'MetodoPago':'Metodo Pago',
    		'Grupal':'Clase Grupal',
		}

		widgets={
			'Local':forms.Select(attrs={'class' : 'forms-control'}),
    		'Mes':forms.Select(attrs={'class' : 'forms-control'}),
    		'Grupal':forms.RadioSelect(attrs={'class' : 'forms-control'}),
		}


class ParticipanteForm(ModelForm):
	class Meta:
		model = Participante
		fields = [
			    'Nombre',
    			'Clase_Perteneciente',
				'Code_Clase',
   				'Local',
    			'Dia',
    			'Horario_Inicio',
    			'Horario_Termino',
			]
		
		labels = {
			'Nombre':'Nombre',
    		'Clase_Perteneciente':'Clase',
			'Code_Clase':'ID Clase',
   			'Local':'Local',
    		'Dia':'Dia',
    		'Horario_Inicio':'Inicio',
    		'Horario_Termino':'Termino',
		}

		widgets = {
			'Nombre' : forms.TextInput(attrs={'class' : 'forms-control','placeholder': 'Primer Nombre & Apellidos'}),
			'Local':forms.Select(attrs={'class' : 'forms-control'}),
    		'Dia':forms.Select(attrs={'class' : 'forms-control'}),
		}

class ParticipanteEventForm(ModelForm):
	class Meta:
		model = ParticipantesEvent
		fields= [
			'ID_Event',
			'EventInscrito',
    		'NombreParticipante',
    		'Escena',
		]

		labels= {
			'EventInscrito' : 'Evento Inscrito',
    		'NombreParticipante' : 'Nombre Participante',
    		'Escena' : 'Escena participante',
		}

		widgets={
			'NombreParticipante' : forms.TextInput(attrs={'class' : 'forms-control','placeholder': 'Primer Nombre & Apellidos'}),
		}
