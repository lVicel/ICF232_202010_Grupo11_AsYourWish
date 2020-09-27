from django.shortcuts import render, redirect#Importamos las Funciones "render"
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
from Base_Profesor.forms import ProfesorForm
from Base_Profesor.models import Profesor
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
@login_required
def Lista_PagProfe(request):
	Lst_Profesor=Profesor.objects.all()
	return render(request,"Lista_Profesor.html",{"Lista_Profesor":Lst_Profesor})


@login_required
def Registrar_PagProfe(request):
	data={
		'form': ProfesorForm()
	}
	if request.method == 'POST':
		Profe= ProfesorForm(request.POST)
		if  Profe.is_valid():
			Profe.save()
			data['mensaje']="Se regristro correctamente el Profesor"
	return render(request,"Registrar_Profesor.html", data)



@login_required
def Modificar_PagProfe(request, id):
	Profe= Profesor.objects.get(id=id)
	data={
		'form':ProfesorForm(instance=Profe)
	}

	if request.method=='POST':
		formulario =  ProfesorForm(data=request.POST, instance=Profe)
		if formulario.is_valid():
			formulario.save()
			data['mensaje']="Se Modifico correctamente el Alumno"
			data['form']=formulario
	return render(request,"Modificar_Profesor.html", data)



@login_required
def Eliminar_PagProfe(request, id):
	Profe=Profesor.objects.get(id=id)
	Profe.delete()
	return redirect("http://127.0.0.1:8000/Listado_Profesor/")


@login_required
def BuscarProfesor(request):
	Busqueda = request.GET.get("Nombre_B")
	Profe = Profesor.objects.all()
	if Busqueda:
		Profe = Profesor.objects.filter(
			Q(NombreProf__icontains=Busqueda)#Revisa cada Campo de "Nombre"
			).distinct()

	return render(request,"Buscar_Profesor.html", {"Profesor_Encontrado":Profe})
