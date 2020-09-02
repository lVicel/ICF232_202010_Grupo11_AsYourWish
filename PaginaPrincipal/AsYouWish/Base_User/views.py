from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class CrearUsuario(CreateView):
    model = User
    template_name = "CrearUsuario.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('Inicio')

# Create your views here.
