from django.shortcuts import render, redirect#Importamos las Funciones "render"
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
from Base_Clase.forms import ClaseForm
from Base_Clase.models import Klase
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
@login_required
def Lista_PagClase(request):
	Lst_Clases=Klase.objects.all()
	return render(request,"Lista_Clase.html",{"Lista_CLASES":Lst_Clases})



@login_required
def Registrar_PagClase(request):
	data={
		'form': ClaseForm()
	}
	if request.method == 'POST':
		Claz = ClaseForm(request.POST)
		if  Claz.is_valid():
			Claz.save()
			data['mensaje']="Se regristro correctamente la Clase"
	return render(request,"Registrar_Clase.html", data)


@login_required
def Modificar_PagClase(request, id):
	Claz= Klase.objects.get(id=id)
	data={
		'form':ClaseForm(instance=Claz)
	}

	if request.method=='POST':
		formulario =  ClaseForm(data=request.POST, instance=Claz)
		if formulario.is_valid():
			formulario.save()
			data['mensaje']="Se Modifico correctamente la Clase"
			data['form']=formulario
	return render(request,"Modificar_Clase.html", data)


@login_required
def Eliminar_PagClase(request, id):
	Claz=Klase.objects.get(id=id)
	Claz.delete()
	return redirect("http://127.0.0.1:8000/Listado_Clase/")


@login_required
def BuscarClase(request):
	Busqueda = request.GET.get("Nombre_B")
	Claz = Klase.objects.all()
	if Busqueda:
		Claz = Klase.objects.filter(
			Q(NombreClas__icontains=Busqueda)#Revisa cada Campo de "NombreClas"
			).distinct()

	return render(request,"Buscar_Clase.html", {"Clase_Encontrada":Claz})