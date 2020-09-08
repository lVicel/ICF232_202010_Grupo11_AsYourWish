from django.shortcuts import render, redirect #Importamos las Funciones Render & Redirect
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.http import HttpResponse
from django.db.models import Q #Importa la funcion para la Barra de Busqueda
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"


# Create your views here.
@login_required
def Inicio_Pag(request):
	return render(request,"Inicio.html")
