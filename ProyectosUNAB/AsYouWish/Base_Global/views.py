from django.shortcuts import render, redirect#Importamos las Funciones "render"
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
#from Base_Global.forms import GlobalForm
from Base_Global.models import EstadoMensual
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
@login_required
def Registro_Mensual(request):
	Lst_Estado=EstadoMensual.objects.all()
	return render(request,"Registro_Estado.html",{"Lista_Estado":Lst_Estado})