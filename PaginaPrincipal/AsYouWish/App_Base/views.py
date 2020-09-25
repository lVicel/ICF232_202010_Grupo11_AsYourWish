from django.shortcuts import render, redirect  # Importamos las Funciones "render"
from django.views.generic import TemplateView  # Importamos las Funciones "TemplateView"
from django.contrib.auth.decorators import login_required  # Importa la Funcion de "login_required"
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Q
from App_Base.forms import AlumnoForm
from App_Base.models import Alumno


# Create your views here.

# Secciond para Inicio
@login_required
def Base_Inicio(request):
    return render(request, "Inicio.html")


@login_required
def Lista_Pag(request):
    Lst_Alumnos = Alumno.objects.all()
    return render(request, "AlumnosRegistrados.html", {"Lista_Alumnos": Lst_Alumnos})


@login_required
def Registrar_Pag(request):
    data = {
        'form': AlumnoForm()
    }
    if request.method == 'POST':
        Alumn = AlumnoForm(request.POST)
        if Alumn.is_valid():
            Alumn.save()
            data['mensaje'] = "Se regristro correctamente el Alumno"
    return render(request, "RegistrarAlumnos.html", data)


@login_required
def Modificar_Pag(request, id):
    Alumn = Alumno.objects.get(id=id)
    data = {
        'form': AlumnoForm(instance=Alumn)
    }

    if request.method == 'POST':
        formulario = AlumnoForm(data=request.POST, instance=Alumn)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Se Modifico correctamente el Alumno"
            data['form'] = formulario
    return render(request, "Modificar_Alumno.html", data)


@login_required
def Eliminar_Pag(request, id):
    Alumn = Alumno.objects.get(id=id)
    Alumn.delete()
    return redirect("http://127.0.0.1:8000/Listado_Alumnos/")


@login_required
def BuscarAlumnos(request):
    Busqueda = request.GET.get("Nombre_B")
    Alumn = Alumno.objects.all()
    if Busqueda:
        Alumn = Alumno.objects.filter(
            Q(Nombre__icontains=Busqueda)  # Revisa cada Campo de "Nombre"
        ).distinct()

    return render(request, "Buscar_Alumno.html", {"Alumno_Encontrado": Alumn})
