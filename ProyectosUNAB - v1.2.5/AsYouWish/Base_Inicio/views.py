from django.shortcuts import render, redirect #Importamos las Funciones Render & Redirect
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.http import HttpResponse
from django.db.models import Q #Importa la funcion para la Barra de Busqueda
from django.contrib.auth.decorators import permission_required, login_required#Importa la Funcion de "login_required"
from .choices import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
#Estas funciones sirven para verificar si el usuario pertenece en ese grupo
def is_basico(Usr):
    return Usr.groups.filter(name='Basico').exists()

def is_in_multiple_groups(Usr):
    return Usr.groups.filter(name__in=['Anfitrion', 'Director']).exists()

def is_anfitrion(Usr):
    return Usr.groups.filter(name='Anfitrion').exists()

def is_director(Usr):
    return Usr.groups.filter(name='Director').exists()

def Pag_Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, 'login.html')

@login_required
def Pag_Inicio(request):
	return render(request,"Seleccion_Disponibles.html")

@login_required
@user_passes_test(is_in_multiple_groups)
def Gestion_Inicio(request):
	return render(request,"Gestion_Inicio.html")
