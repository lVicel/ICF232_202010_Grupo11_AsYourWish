from django.shortcuts import render, redirect #Importamos las Funciones Render & Redirect
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.http import HttpResponse
from django.db.models import Q #Importa la funcion para la Barra de Busqueda
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from .forms import ResidenciasForm

def selResidencia(request):
    context = {}
    form = ResidenciasForm()
    context['form'] = form
    if request.GET:
        temp = request.GET['residencias_field']
        print(temp)
        return redirect('/accounts/login/')
    return render(request, "Selección_Residencia.html", context)

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

@login_required
def Pag_Inicio(request):
    return render(request,"Seleccion_Disponibles.html")

@login_required
def Gestion_Inicio(request):
    return render(request,"Gestion_Inicio.html")


