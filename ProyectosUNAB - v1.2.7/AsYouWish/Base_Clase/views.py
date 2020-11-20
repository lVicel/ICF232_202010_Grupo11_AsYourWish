from django.shortcuts import render, redirect#Importamos las Funciones "render"
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
from django.contrib import messages
from Base_Clase.forms import ClaseForm
from Base_Alumno.forms import ParticipanteForm
from Base_Clase.models import Klase
from Base_Alumno.models import Participante
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .filters import Filtro_Clases
import logging

# Create your views here.
#---------------Clases---------------
@login_required
def Lista_Clases(request):
	Lst_Clases=Klase.objects.all()
	Filtro_Cls = Filtro_Clases(request.GET, queryset=Lst_Clases)
	Lst_Clases = Filtro_Cls.qs
	
	return render(request,"Clases/Lista_Clase.html",{"Lista_HTML":Lst_Clases, 'Filtro':Filtro_Cls})



@login_required
def Registrar_Clases(request):
	data={
		'form': ClaseForm()
	}
	if request.method == 'POST':
		Claz = ClaseForm(request.POST)
		if  Claz.is_valid():
			Claz.save()
			data['mensaje']="Registro Completado"
		else:
			data['mensaje']="Ocurrio un ERROR al Registrar"
	return render(request,"Clases/Registrar_Clase.html", data)


@login_required
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
def Eliminar_PagClase(request, id):
	Claz=Klase.objects.get(id=id)
	Claz.delete()
	return redirect("/Listado_Clases/")



#---------------Participantes---------------

@login_required
def Participantes_Clase(request, id):
	Claz= Klase.objects.get(id=id)
	Code_Cls = Claz.id
	Prtic = Participante.objects.filter(Code_Clase=Code_Cls)
	context={"Lista_HTML":Prtic, "Clase_Select":Claz}
	
	return render(request, "Participantes/Participantes_Clase.html", context)

@login_required
def Registrar_Participante(request, id):
	Claz= Klase.objects.get(id=id)

	Nombre_Dft = Claz.NombreClas
	Local_Dft = Claz.Local
	Code_Dft = Claz.id
	Inicio_Dft = Claz.ClassInicio
	Termino_Dft = Claz.ClassTermino

	initial_data={
		'Clase_Perteneciente':Nombre_Dft,
		'Local' : Local_Dft,
		'Code_Clase':Code_Dft,
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
			Prtic.save()
			data['mensaje']="Participante Registrado"
	return render(request,"Participantes/Registrar_Participante.html", data)

@login_required
def Eliminar_Participante(request, id):
	Prtic=Participante.objects.get(id=id)
	Prtic.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#-------------------------------------------------------------------------



#---------------Asistencias---------------
def PagInicio_Asistencias(request):
	Clases_Disponibles=Klase.objects.all()
	Filtro_Clase = Filtro_Clases(request.GET, queryset=Clases_Disponibles)
	Clases_Disponibles = Filtro_Clase.qs
	return render(request, "Asistencias/Filtro_Busqueda.html", {'Lista_HTML':Clases_Disponibles, 'Filtro':Filtro_Clase})



def Lista_Asistencia(request, id):
    Claz= Klase.objects.get(id=id)
    Class_ID=Claz.id
    Prtic = Participante.objects.filter(Code_Clase__icontains=Class_ID)
    return render(request,"Asistencias/Asistencias.html", {'Lista_HTML':Prtic})

def Registrar_Asistencia(request):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    mensaje = "No hay alumnos para registrar"
    mensajeFinal = ""
    if request.method == "POST":
        parti = request.POST.getlist('participante')
        logger.info(parti)
        logger.info("largo")
        logger.info(len(parti))
        if(len(parti) > 0): 
            if(len(parti) > 1):     
                mensaje = "Los alumnos : "
                mensajeFinal = " fueron registrados correctamente"     
            else:
                mensaje = "El alumno : "
                mensajeFinal = " fue registrado correctamente"  
            contador = 1            
            for id in parti:
                objParti = Participante.objects.get(pk=id)
                objParti.AsistTotales = objParti.AsistTotales + 1
                logger.info(objParti.Nombre)
                logger.info(objParti.AsistTotales)
                mensaje = mensaje + objParti.Nombre
                if(contador == len(parti) - 1 and len(parti) > 1):
                    mensaje = mensaje + " y "
                elif(len(parti) > 1 and contador < len(parti) - 1):
                    mensaje = mensaje + ", "                                        
                objParti.save()     
                contador = contador + 1
            mensaje = mensaje + mensajeFinal
    Clases_Disponibles=Klase.objects.all()
    Filtro_Clase = Filtro_Clases(request.GET, queryset=Clases_Disponibles)
    Clases_Disponibles = Filtro_Clase.qs
    messages.success(request,mensaje)
    return render(request, "Asistencias/Filtro_Busqueda.html", {'Lista_HTML':Clases_Disponibles, 'Filtro':Filtro_Clase})
			
