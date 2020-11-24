from django.shortcuts import render, redirect#Importamos las Funciones "render"
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
from Base_Alumno.forms import AlumnoForm, PagosForm
from Base_Alumno.models import Alumno, Participante, PagosAlumno
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from Base_Alumno.filters import Filtro_Alumno
from Base_Local.models import Local
from Base_Global.models import EstadoMensual
from Base_User.decorators import allowed_users

# Create your views here.
#---------------Alumnos---------------
@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion'])
def Lista_Alumnos(request):
	Lst_Alumnos=Alumno.objects.all().order_by('Nombre')
	Filtro_Alumn = Filtro_Alumno(request.GET, queryset=Lst_Alumnos)
	Lst_Alumnos = Filtro_Alumn.qs
	return render(request,"Alumnos/Lista_Alumno.html",{"Lista_HTML":Lst_Alumnos, 'Filtro':Filtro_Alumn})


@login_required
@allowed_users(allowed_roles=['Director'])
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
@allowed_users(allowed_roles=['Director'])
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
@allowed_users(allowed_roles=['Director'])
def Eliminar_Alumnos(request, id):
	Alumn=Alumno.objects.get(id=id)
	Alumn.delete()
	return redirect("/Listado_Alumnos/")


#---------------Clases/Locales---------------
@login_required
@allowed_users(allowed_roles=['Director','Anfitrion'])
def ClasesLocales(request, Nombre):
	Alumn= Alumno.objects.get(Nombre=Nombre)
	Nombre_Alum=Alumn.Nombre
	Pertenece = Participante.objects.filter(Nombre__icontains=Nombre_Alum).order_by('Clase_Perteneciente')
	context={"Lista_HTML":Pertenece}
	return render(request, "Clases-Locales/Lista_ClasesLocales.html", context)

#-------------------------------------------------------------------------------------------------------

#---------------Pagos---------------
@login_required
@allowed_users(allowed_roles=['Director','Anfitrion'])
def Pagos_Alumno(request, id):
	Alumn = Alumno.objects.get(id=id)
	Alumno_Slt = Alumn.id
	PAGO = PagosAlumno.objects.filter(id_Alumno__icontains=Alumno_Slt)
	
	context = {"Lista_HTML":PAGO, "Alumn_Select":Alumn}
	
	return render(request, "Pagos/Lista_Pago.html", context)


	
@login_required
@allowed_users(allowed_roles=['Director'])
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
		"Alumn_Select":Alumn,
	}
	if request.method == 'POST':
		Prtic = PagosForm(request.POST)

		if  Prtic.is_valid():
			#Aqui se reciben los Valores del Formulario
			New_D = Prtic.cleaned_data
			New_Local = New_D['Local']
			New_Anno = New_D['Anno']
			New_Mes = New_D['Mes']
			New_Ingreso = New_D['IngresoAlumno']
			#-------------------------------------------
			Prtic.save()
			data['mensaje']="Registro Completado"
			if Local.objects.filter(Local = New_Local).filter(Anno = New_Anno).filter(Mes = New_Mes).exists():
				Old_Lcl = Local.objects.filter(Local = New_Local).filter(Anno = New_Anno).filter(Mes = New_Mes).first()
				Old_Lcl.TotalIngresos = Old_Lcl.TotalIngresos + New_Ingreso
				Old_Lcl.save()
				#-------------
				Old_Estado = EstadoMensual.objects.filter(Anno = New_Anno).filter(Mes = New_Mes).first()
				Old_Estado.TotalIngresos = Old_Estado.TotalIngresos + New_Ingreso
				Old_Estado.save()

			else:
				New_LclPago=Local(Local=New_Local,Anno=New_Anno,Mes=New_Mes,TotalIngresos=New_Ingreso)
				New_LclPago.save()		
				New_GlobalPago=EstadoMensual(Anno=New_Anno,Mes=New_Mes,TotalIngresos=New_Ingreso)
				New_GlobalPago.save()
		else:
			data['mensaje']="Ocurrio un ERROR al Registrar"
	
	return render(request,"Pagos/Registrar_Pago.html", data)


@login_required
@allowed_users(allowed_roles=['Director'])
def Eliminar_Pagos(request, id):
	PAGO=PagosAlumno.objects.get(id=id)
	New_Local = PAGO.Local
	New_Anno = PAGO.Anno
	New_Mes = PAGO.Mes
	New_Ingreso = PAGO.IngresoAlumno
	
	#Aqui se eliminan los Restan los Ingresos Registrados
	Old_Lcl = Local.objects.filter(Local = New_Local).filter(Anno = New_Anno).filter(Mes = New_Mes).first()
	Old_Lcl.TotalIngresos = Old_Lcl.TotalIngresos - New_Ingreso
	if Old_Lcl.TotalIngresos == 0:
		Old_Lcl.delete()
	else:
		Old_Lcl.save()
	Old_Estado = EstadoMensual.objects.filter(Anno = New_Anno).filter(Mes = New_Mes).first()
	Old_Estado.TotalIngresos = Old_Estado.TotalIngresos - New_Ingreso
	if Old_Estado.TotalIngresos == 0:
		Old_Estado.delete()
	else:
		Old_Estado.save()
	#------------------------------------------------
	PAGO.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))