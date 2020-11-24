from django.shortcuts import render, redirect #Importamos las Funciones Render & Redirect
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.http import HttpResponse
from django.db.models import Q #Importa la funcion para la Barra de Busqueda
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
from Base_User.decorators import allowed_users

# Create your views here.

@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion','Basico'])
def Pag_Inicio(request):
	return render(request,"Seleccion_Disponibles.html")

@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion'])
def Gestion_Inicio(request):
	return render(request,"Gestion_Inicio.html")
