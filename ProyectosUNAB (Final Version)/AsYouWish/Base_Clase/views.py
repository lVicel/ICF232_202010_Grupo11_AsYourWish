from django.shortcuts import render, redirect#Importamos las Funciones "render"
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
from django.contrib import messages
from Base_Clase.forms import ClaseForm
from Base_Alumno.forms import ParticipanteForm
from Base_Clase.models import Klase
from Base_Alumno.models import Participante, Alumno
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .filters import Filtro_Clases
import logging
from Base_User.decorators import allowed_users
from Base_Profesor.models import Profesor

# Create your views here.
#---------------Clases---------------
@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion'])
def Lista_Clases(request):
	Lst_Clases=Klase.objects.all().order_by('NombreClas')
	Filtro_Cls = Filtro_Clases(request.GET, queryset=Lst_Clases)
	Lst_Clases = Filtro_Cls.qs
	return render(request,"Clases/Lista_Clase.html",{"Lista_HTML":Lst_Clases, 'Filtro':Filtro_Cls})



@login_required
@allowed_users(allowed_roles=['Director'])
def Registrar_Clases(request):
	data={
		'form': ClaseForm()
	}
	if request.method == 'POST':
		Claz = ClaseForm(request.POST)
		if  Claz.is_valid():
			#Aqui se reciben los Valores del Formulario
			New_D = Claz.cleaned_data
			New_Nombre = New_D['Profesor']
			#-------------------------------------------
			if Profesor.objects.filter(NombreProf = New_Nombre).exists():
				Claz.save()
				data['mensaje']="Registro Completado"
			else:
				data['mensaje']="No esta Registrado el Profesor"
		else:
			data['mensaje']="Ocurrio un ERROR al Registrar"
	return render(request,"Clases/Registrar_Clase.html", data)


@login_required
@allowed_users(allowed_roles=['Director'])
def Modificar_Clases(request, id):
	Claz= Klase.objects.get(id=id)
	data={
		'form':ClaseForm(instance=Claz)
	}

	if request.method=='POST':
		formulario =  ClaseForm(data=request.POST, instance=Claz)
		if formulario.is_valid():
			formulario.save()
			data['mensaje']="Modificacion Completada"
			data['form']=formulario
		else:
			data['mensaje']="Ocurrio un ERROR al Modificar"
	return render(request,"Clases/Modificar_Clase.html", data)


@login_required
@allowed_users(allowed_roles=['Director'])
def Eliminar_PagClase(request, id):
	Claz=Klase.objects.get(id=id)
	Code_Cls = Claz.id
	Prtic = Participante.objects.filter(Code_Clase=Code_Cls)

	for x in Prtic:
		Prtic.delete()

	Claz.delete()
	return redirect("/Listado_Clases/")



#---------------Participantes---------------

@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion'])
def Participantes_Clase(request, id):
	Claz= Klase.objects.get(id=id)
	Code_Cls = Claz.id
	Prtic = Participante.objects.filter(Code_Clase=Code_Cls).order_by('Nombre')
	context={"Lista_HTML":Prtic, "Clase_Select":Claz}
	
	return render(request, "Participantes/Participantes_Clase.html", context)

@login_required
@allowed_users(allowed_roles=['Director'])
def Registrar_Participante(request, id):
	Claz= Klase.objects.get(id=id)

	Nombre_Dft = Claz.NombreClas
	Code_Dft = Claz.id
	Local_Dft = Claz.Local
	Dia_Dft=Claz.Dia
	Inicio_Dft = Claz.ClassInicio
	Termino_Dft = Claz.ClassTermino

	initial_data={
		'Clase_Perteneciente':Nombre_Dft,
		'Code_Clase':Code_Dft,
		'Local' : Local_Dft,
		'Dia': Dia_Dft,
		'Horario_Inicio':Inicio_Dft,
		'Horario_Termino':Termino_Dft,
	}

	data={
		'form': ParticipanteForm(initial=initial_data),
		'Clase_Select':Claz,
	}
	if request.method == 'POST':
		Prtic = ParticipanteForm(request.POST)
		if  Prtic.is_valid():
			#Aqui se reciben los Valores del Formulario
			New_D = Prtic.cleaned_data
			New_Nombre = New_D['Nombre']
			#-------------------------------------------
			if Participante.objects.filter(Nombre = Prtic.cleaned_data["Nombre"],Horario_Inicio=Prtic.cleaned_data["Horario_Inicio"],Local=Prtic.cleaned_data["Local"]).exists():
				data['mensaje']="El Alumno Ya esta registrado"
			else:
				if Alumno.objects.filter(Nombre = New_Nombre).exists():
					Prtic.save()
					data['mensaje']="Participante Registrado"
					Alumn =  Alumno.objects.filter(Nombre = New_Nombre).first()
					if Alumn.Genero == 'Hombre':
						Claz.AsistHombres = Claz.AsistHombres + 1
						Claz.AsistTotales = Claz.AsistTotales + 1
						Claz.save()
					else:
						Claz.AsistMujeres = Claz.AsistMujeres + 1
						Claz.AsistTotales = Claz.AsistTotales + 1
						Claz.save()
				else:
					data['mensaje']="El Alumno No esta registrado"
	return render(request,"Participantes/Registrar_Participante.html", data)

@login_required
@allowed_users(allowed_roles=['Director'])
def Eliminar_Participante(request, id):
	Prtic=Participante.objects.get(id=id)

	Nombre_Alumn = Prtic.Nombre #Recive el Nombre del Participante
	Codigo_Clase = Prtic.Code_Clase #Recive el ID de la Clase

	Alumn =  Alumno.objects.filter(Nombre=Nombre_Alumn).first()
	Claz = Klase.objects.filter(id = Codigo_Clase).first()
	
	if Alumn.Genero == 'Hombre':
		Claz.AsistHombres = Claz.AsistHombres - 1
		Claz.AsistTotales = Claz.AsistTotales - 1
		Claz.save()
	else:
		Claz.AsistMujeres = Claz.AsistMujeres - 1
		Claz.AsistTotales = Claz.AsistTotales - 1
		Claz.save()

	Prtic.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#-------------------------------------------------------------------------



#---------------Asistencias---------------
@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion','Basico'])
def PagInicio_Asistencias(request):
	Clases_Disponibles=Klase.objects.all().order_by('NombreClas')

	Filtro_Clase = Filtro_Clases(request.GET, queryset=Clases_Disponibles)
	Clases_Disponibles = Filtro_Clase.qs
	return render(request, "Asistencias/Filtro_Busqueda.html", {'Lista_HTML':Clases_Disponibles, 'Filtro':Filtro_Clase})


@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion','Basico'])
def Lista_Asistencia(request, id):
	Claz= Klase.objects.get(id=id)
	Class_ID=Claz.id
	Prtic = Participante.objects.filter(Code_Clase__icontains=Class_ID).order_by('Nombre')

	return render(request,"Asistencias/Asistencias.html", {'Lista_HTML':Prtic, 'Clase_Select':Claz})

@login_required
@allowed_users(allowed_roles=['Director','Basico'])
def Registrar_Asistencia(request):	
	logging.basicConfig(level=logging.INFO) #Revisa si el CheckBox esta marcado
    
	if request.method == "POST":
		parti = request.POST.getlist('participante') #se obtiene el participante
		for id in parti:
		    objParti = Participante.objects.get(pk=id) #se obtiene participante para verificar asistencia
		    objParti.AsistTotales = objParti.AsistTotales + 1 # aumenta asistencia en 1 si el participante es seleccionado                                        
		    objParti.save()
			
		messages.info(request, 'Asistencia Registrada')
		return redirect('Inicio_Asistencias/')
	return render(request,"Asistencias/Asistencias.html")
		
			
