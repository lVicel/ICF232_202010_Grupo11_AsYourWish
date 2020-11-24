from django.shortcuts import render, redirect#Importamos las Funciones "render"
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
from Base_Evento.forms import EventoForm
from Base_Alumno.forms import ParticipanteEventForm
from Base_Evento.models import Evento
from Base_Alumno.models import ParticipantesEvent, Alumno
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from Base_Evento.filters import Filtro_Event
from Base_User.decorators import allowed_users

# Create your views here.
#---------------Eventos---------------
@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion'])
def Lista_Eventos(request):
	Lst_Evento=Evento.objects.all()
	Filtro_Ev=Filtro_Event(request.GET, queryset=Lst_Evento)
	Lst_Evento = Filtro_Ev.qs

	context = {"Lista_HTML":Lst_Evento, "Filtro":Filtro_Ev}
	return render(request,"Eventos/Lista_Evento.html",context)


@login_required
@allowed_users(allowed_roles=['Director'])
def Registrar_Eventos(request):
	data={
		'form': EventoForm()
	}
	if request.method == 'POST':
		Event= EventoForm(request.POST)
		if  Event.is_valid():
			Event.save()
			data['mensaje']="Registro Completado"
		else:
			data['mensaje']="Ocurrio un ERROR al Registrar"
	return render(request,"Eventos/Registrar_Evento.html", data)


@login_required
@allowed_users(allowed_roles=['Director'])
def Modificar_Eventos(request, id):
	Event= Evento.objects.get(id=id)
	data={
		'form':EventoForm(instance=Event)
	}

	if request.method=='POST':
		formulario =  EventoForm(data=request.POST, instance=Event)
		if formulario.is_valid():
			formulario.save()
			data['mensaje']="Modificacion Completada"
			data['form']=formulario
		else:
			data['mensaje']="Ocurrio un ERROR al Modificar"
	return render(request,"Eventos/Modificar_Evento.html", data)


@login_required
@allowed_users(allowed_roles=['Director'])
def Eliminar_Eventos(request, id):
	Event=Evento.objects.get(id=id)
	Code_Event = Event.id
	Prtic = ParticipantesEvent.objects.filter(ID_Event__icontains=Code_Event)

	for x in Prtic:
		Prtic.delete()
		
	Event.delete()
	return redirect("/Listado_Eventos/")



#---------------------------------------------------------------------------------------------------------------------------------------

#---------------Participantes Eventos---------------------------------------------------------------------------------------------------
@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion'])
def Participantes_Evento(request, id):
	Event=Evento.objects.get(id=id)
	Code_Event=Event.id
	Prtic = ParticipantesEvent.objects.filter(ID_Event__icontains=Code_Event)
	context={"Lista_HTML":Prtic, "Event_Select":Event}
	return render(request, "ParticipantesEvent/Participantes_Evento.html", context)

@login_required
@allowed_users(allowed_roles=['Director'])
def Registrar_ParticipanteEvent(request, id):
	Event=Evento.objects.get(id=id)

	Nombre_Dft = Event.NombreEvent
	ID_Dft = Event.id
	initial_data={
		'EventInscrito':Nombre_Dft,
		'ID_Event': ID_Dft,
	}

	data={
		'form': ParticipanteEventForm(initial=initial_data),
		"Event_Select": Event,
	}
	if request.method == 'POST':
		Prtic = ParticipanteEventForm(request.POST)
		if  Prtic.is_valid():
			#Aqui se reciben los Valores del Formulario
			New_D = Prtic.cleaned_data
			New_Nombre = New_D['NombreParticipante']
			#-------------------------------------------
			if Alumno.objects.filter(Nombre = New_Nombre).exists():
				Prtic.save()
				data['mensaje']="Participante Registrado"
			else:
				data['mensaje']="El Alumno No esta registrado"
	return render(request,"ParticipantesEvent/Registrar_ParticipanteEvent.html", data)

@login_required
@allowed_users(allowed_roles=['Director'])
def Eliminar_ParticipanteEvent(request, id):
	Prtic=ParticipantesEvent.objects.get(id=id)
	Prtic.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

