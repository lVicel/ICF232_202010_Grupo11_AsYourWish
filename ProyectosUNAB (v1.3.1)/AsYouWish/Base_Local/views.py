from django.shortcuts import render, redirect #Importamos las Funciones Render & Redirect
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.http import HttpResponse
from django.db.models import Q #Importa la funcion para la Barra de Busqueda
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
from Base_Local.models import Local
from Base_User.decorators import allowed_users

# Create your views here.
@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion'])
def Academias_AsYouWish(request):
	return render(request,"Inicio_Locales.html")

@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion'])
def Estado_CasaMatriz(request):
	Lcl = Local.objects.filter(Local__icontains="Casa Matriz")
	return render(request,"Locales/CasaMatriz.html",{'Lista_HTML':Lcl})

@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion'])
def Estado_Bellavista(request):
	Lcl = Local.objects.filter(Local__icontains="Bellavista")
	return render(request,"Locales/Bellavista.html",{'Lista_HTML':Lcl})

@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion'])
def Estado_Providencia(request):
	Lcl = Local.objects.filter(Local__icontains="Providencia")
	return render(request,"Locales/Providencia.html",{'Lista_HTML':Lcl})

@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion'])
def Estado_LaFlorida(request):
	Lcl = Local.objects.filter(Local__icontains="La Florida")
	return render(request,"Locales/LaFlorida.html",{'Lista_HTML':Lcl})