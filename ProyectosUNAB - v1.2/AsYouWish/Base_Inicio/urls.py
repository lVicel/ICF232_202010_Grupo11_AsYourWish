from django.conf.urls import url#Importamos las Funciones "url"
from django.urls import path, include#Importamos las Funciones de "Path" & "Include"
from . import views #Importamos las Vistas(views.py) que se encuentran en App_Base

urlpatterns=[
path('accounts/', include('django.contrib.auth.urls')),#URL para el Login
url(r'^$',views.Pag_Inicio),#Seleccion_Disponibles.html
url('Inicio_Gestion/',views.Gestion_Inicio),#Gestion_Inicio.html
]