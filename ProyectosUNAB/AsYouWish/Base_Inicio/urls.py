from django.conf.urls import url#Importamos las Funciones "url"
from django.urls import path, include#Importamos las Funciones de "Path" & "Include"
from Base_Inicio import views #Importamos las Vistas(views.py) que se encuentran en App_Base


urlpatterns=[
path('accounts/', include('django.contrib.auth.urls')),#Creamos una URL para nuestro Login
url(r'^$',views.Inicio_Pag),#Este es el URL de  de la Vista "Base_Inicio"
path('accounts/', include('django.contrib.auth.urls')),#Creamos una URL para nuestro Login
]