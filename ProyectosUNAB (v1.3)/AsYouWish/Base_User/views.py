from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from Base_User.forms import UsuarioForm
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.models import Group
from .decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['Director'])
def CrearUsuario(request):
    if request.method == 'POST':
        first_name =  request.POST['first_name']
        last_name =  request.POST['last_name']
        username =  request.POST['username']
        password1 =  request.POST['password1']
        password2 =  request.POST['password2']
        email =  request.POST['email']
        group = request.POST['group']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Nombre de Usuario ya registrado')
                return redirect('CrearUsuarios/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email ya registrado')
                return redirect('CrearUsuarios/')

            else:  
                user = User.objects.create_user(username=username, password=password1, email= email, first_name=first_name, last_name=last_name)
                user.save()
                my_group = Group.objects.get(name = group) 
                user.groups.add(my_group)
                messages.info(request, 'Usuario registrado')
                return redirect('CrearUsuarios/')

    else:
        return render(request,'CrearUsuarios.html') 
    return render(request, 'CrearUsuarios.html')

@login_required
@allowed_users(allowed_roles=['Director'])
def EliminarUsuario(request, id):
    Usr=User.objects.get(id=id)
    Usr.delete()
    return redirect("/Listado_Usario/")


@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion'])
def Lista_Usuarios(request):
	Lst_User=User.objects.all()
	return render(request,"Lista_User.html",{"Lista_HTML":Lst_User})

# Create your views here.
