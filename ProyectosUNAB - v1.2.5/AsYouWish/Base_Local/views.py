from django.shortcuts import render, redirect #Importamos las Funciones Render & Redirect
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.http import HttpResponse
from django.db.models import Q #Importa la funcion para la Barra de Busqueda
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
#Estas funciones sirven para verificar si el usuario pertenece en ese grupo
def is_basico(Usr):
    return Usr.groups.filter(name='Basico').exists()

def is_anfitrion(Usr):
    return Usr.groups.filter(name='Anfitrion').exists()

def is_director(Usr):
    return Usr.groups.filter(name='Director').exists()

@login_required
def Academias_AsYouWish(request):
	return render(request,"Inicio_Locales.html")


@login_required
def Registro_Providencia(request):
	Lst_Providencia=Local.objects.all()
	return render(request,"Providencia.html",{"Lista_Providencia":Lst_Providencia})