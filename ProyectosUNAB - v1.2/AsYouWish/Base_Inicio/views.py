from django.shortcuts import render, redirect #Importamos las Funciones Render & Redirect
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.http import HttpResponse
from django.db.models import Q #Importa la funcion para la Barra de Busqueda
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
from .choices import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
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
def Gestion_Inicio(request):
	return render(request,"Gestion_Inicio.html")
