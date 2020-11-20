from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test


#Estas funciones sirven para verificar si el usuario pertenece en ese grupo
def is_basico(Usr):
    return Usr.groups.filter(name='Basico').exists()

def is_anfitrion(Usr):
    return Usr.groups.filter(name='Anfitrion').exists()

def is_director(Usr):
    return Usr.groups.filter(name='Director').exists()



@user_passes_test(is_director)
def CrearUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            residencia = form.cleaned_data.get('residencia')
            user = authenticate(username=username, password=raw_password, residencia=residencia)
            login(request, user)
            messages.success(request, 'El usuario ha sido creado')
            return redirect("/Listado_Usario/")
    else:
        form = UsuarioForm()
    return render(request, 'CrearUsuarios.html', {'form': form})


def Lista_Usuarios(request):
    Lst_User = User.objects.all()
    return render(request, "Lista_User.html", {"Lista_HTML": Lst_User})

@user_passes_test(is_director)
def Asignar_Basico(request,id):
    Usr = User.objects.get(id=id)
    Basico = Group.objects.get(name='Basico')
    Basico.user_set.add(Usr)
    messages.success(request, 'El usuario ha sido asignado a Basico')
    return redirect("/Listado_Usario/")

@user_passes_test(is_director)
def Eliminar_Basico(request,id):
    Usr = User.objects.get(id=id)
    Basico = Group.objects.get(name='Basico')
    Basico.user_set.remove(Usr)
    messages.success(request, 'El usuario ha sido removido de Basico')
    return redirect("/Listado_Usario/")

@user_passes_test(is_director)
def Asignar_Anfitrion(request,id):
    Usr = User.objects.get(id=id)
    Anfitrion = Group.objects.get(name='Anfitrion')
    Anfitrion.user_set.add(Usr)
    messages.success(request, 'El usuario ha sido asignado a Anfitrion')
    return redirect("/Listado_Usario/")

@user_passes_test(is_director)
def Eliminar_Anfitrion(request,id):
    Usr = User.objects.get(id=id)
    Anfitrion = Group.objects.get(name='Anfitrion')
    Anfitrion.user_set.remove(Usr)
    messages.success(request, 'El usuario ha sido removido de Anfitrion')
    return redirect("/Listado_Usario/")

@user_passes_test(is_director)
def Asignar_Director(request,id):
    Usr = User.objects.get(id=id)
    Director = Group.objects.get(name='Director')
    Director.user_set.add(Usr)
    messages.success(request, 'El usuario ha sido asignado a Director')
    return redirect("/Listado_Usario/")

@user_passes_test(is_director)
def Eliminar_Director(request,id):
    Usr = User.objects.get(id=id)
    Director = Group.objects.get(name='Director')
    Director.user_set.remove(Usr)
    messages.success(request, 'El usuario ha sido removido de Director')
    return redirect("/Listado_Usario/")

@user_passes_test(is_director)
def Eliminar_Usuarios(request, id):
    Usr = User.objects.get(id = id)
    Usr.delete()
    messages.success(request, 'El usuario ha sido eliminado')
    return redirect("/Listado_Usario/")

# Los 3 Usuarios o Grupos eran los Siguientes:
# Basico --> Solo podra ser capaz de registrar las Asistencias de Alumnos
#
# Anfitrion-->Solo podra visualizar los Datos de las Tablas, pero NO capaz de Registrar, Modificar o Eliminar algun tipo de Objeto o Dato
#
# Director-->Ademas de visualizar los Datos de las Tablas, este tambien podra registrar, Modifcar, o Eliminar algun tipo de Objeto o Dato.
