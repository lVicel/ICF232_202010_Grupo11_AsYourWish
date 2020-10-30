from django.shortcuts import render, redirect#Importamos las Funciones "render"
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
from Base_Alumno.forms import AlumnoForm, PagosForm
from Base_Alumno.models import Alumno, Participante, PagosAlumno
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from Base_Alumno.filters import Filtro_Alumno

# Create your views here.
#---------------Alumnos---------------
@login_required
def Lista_Alumnos(request):
	Lst_Alumnos=Alumno.objects.all()
	Filtro_Alumn = Filtro_Alumno(request.GET, queryset=Lst_Alumnos)
	Lst_Alumnos = Filtro_Alumn.qs
	return render(request,"Alumnos/Lista_Alumno.html",{"Lista_HTML":Lst_Alumnos, 'Filtro':Filtro_Alumn})


@login_required
def Registrar_Alumnos(request):
	data={
		'form': AlumnoForm()
	}
	if request.method == 'POST':
		Alumn= AlumnoForm(request.POST)
		if  Alumn.is_valid():
			Alumn.save()
			data['mensaje']="Registro Completado"
		else:
			data['mensaje']="Ocurrio un ERROR al Registrar"
	return render(request,"Alumnos/Registrar_Alumno.html", data)


@login_required
def Modificar_Alumnos(request, id):
	Alumn= Alumno.objects.get(id=id)
	data={
		'form':AlumnoForm(instance=Alumn)
	}

	if request.method=='POST':
		formulario =  AlumnoForm(data=request.POST, instance=Alumn)
		if formulario.is_valid():
			formulario.save()
			data['mensaje']="Modificacion Completada"
			data['form']=formulario
		else:
			data['mensaje']="Ocurrio un ERROR al Modificar"
	return render(request,"Alumnos/Modificar_Alumno.html", data)

@login_required
def Eliminar_Alumnos(request, id):
	Alumn=Alumno.objects.get(id=id)
	Alumn.delete()
	return redirect("/Listado_Alumnos/")


#---------------Clases/Locales---------------
@login_required
def ClasesLocales(request, Nombre):
	Alumn= Alumno.objects.get(Nombre=Nombre)
	Nombre_Alum=Alumn.Nombre
	Pertenece = Participante.objects.filter(Nombre__icontains=Nombre_Alum)
	context={"Lista_HTML":Pertenece}
	return render(request, "Clases-Locales/Lista_ClasesLocales.html", context)

#-------------------------------------------------------------------------------------------------------

#---------------Pagos---------------
@login_required
def Pagos_Alumno(request, id):
	Alumn = Alumno.objects.get(id=id)
	Alumno_Slt = Alumn.id
	PAGO = PagosAlumno.objects.filter(id_Alumno__icontains=Alumno_Slt)
	
	context = {"Lista_HTML":PAGO, "Alumn_Select":Alumn}
	
	return render(request, "Pagos/Lista_Pago.html", context)



@login_required
def Registrar_Pago(request, id):
	Alumn = Alumno.objects.get(id=id)
	
	ID_Dft = Alumn.id
	RUT_Dft = Alumn.RUT
	Nombre_Dft = Alumn.Nombre

	initial_data={
		'id_Alumno': ID_Dft,
		'RUT':RUT_Dft,
		'Nombre':Nombre_Dft,
	}

	data={
		'form': PagosForm(initial=initial_data),
		"Alumn_Select":Alumn
	}
	if request.method == 'POST':
		Prtic = PagosForm(request.POST)
		if  Prtic.is_valid():
			Prtic.save()
			data['mensaje']="Registro Completado"
		else:
			data['mensaje']="Ocurrio un ERROR al Registrar"
	
	return render(request,"Pagos/Registrar_Pago.html", data)


@login_required
def Eliminar_Pagos(request, id):
	PAGO=PagosAlumno.objects.get(id=id)
	PAGO.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))