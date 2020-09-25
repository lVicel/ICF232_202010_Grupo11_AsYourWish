from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from Base_User.forms import UsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView

def CrearUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UsuarioForm()
    return render(request, 'CrearUsuarios.html',{'form': form})

# Create your views here.
