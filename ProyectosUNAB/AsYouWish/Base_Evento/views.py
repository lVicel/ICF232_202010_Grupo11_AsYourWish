from django.shortcuts import render, redirect#Importamos las Funciones "render"
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
from Base_Evento.forms import EventoForm
from Base_Evento.models import Evento
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
@login_required
def Lista_PagEvento(request):
	Lst_Evento=Evento.objects.all()
	return render(request,"Lista_Evento.html",{"Lista_Eventos":Lst_Evento})


@login_required
def Registrar_PagEvento(request):
	data={
		'form': EventoForm()
	}
	if request.method == 'POST':
		Event= EventoForm(request.POST)
		if  Event.is_valid():
			Event.save()
			data['mensaje']="Se regristro correctamente el Evento"
	return render(request,"Registrar_Evento.html", data)


@login_required
def Modificar_PagEvento(request, id):
	Event= Evento.objects.get(id=id)
	data={
		'form':EventoForm(instance=Event)
	}

	if request.method=='POST':
		formulario =  EventoForm(data=request.POST, instance=Event)
		if formulario.is_valid():
			formulario.save()
			data['mensaje']="Se Modifico correctamente el Evento"
			data['form']=formulario
	return render(request,"Modificar_Evento.html", data)

@login_required
def Eliminar_PagEvento(request, id):
	Event=Evento.objects.get(id=id)
	Event.delete()
	return redirect("http://127.0.0.1:8000/Listado_Evento/")


@login_required
def BuscarEventos(request):
	Busqueda = request.GET.get("Nombre_B")
	Event = Evento.objects.all()
	if Busqueda:
		Event = Evento.objects.filter(
			Q(NombreEvent__icontains=Busqueda)#Revisa cada Campo de "Nombre"
			).distinct()

	return render(request,"Buscar_Evento.html", {"Evento_Encontrado":Event})