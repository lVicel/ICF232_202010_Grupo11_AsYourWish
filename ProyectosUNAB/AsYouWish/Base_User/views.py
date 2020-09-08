from django.shortcuts import render
from django.urls import reverse_lazy
from Base_User.forms import UsuarioForm
from django.contrib.auth.models import User
from django.views.generic import CreateView

class CrearUsuario(CreateView):
    model = User
    template_name = "CrearUsuarios.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')
# Create your views here.
