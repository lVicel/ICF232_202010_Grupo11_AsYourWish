from django.shortcuts import render, redirect#Importamos las Funciones "render"
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.contrib.auth.decorators import login_required #Importa la Funcion de "login_required"
#from Base_Global.forms import GlobalForm
from Base_Global.models import EstadoMensual
from django.http import HttpResponse
from django.db.models import Q
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
def Registro_Mensual(request):
	Lst_Estado=EstadoMensual.objects.all()
	return render(request,"Registro_Estado.html",{"Lista_HTML":Lst_Estado})