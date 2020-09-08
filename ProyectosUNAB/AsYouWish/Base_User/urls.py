from django.conf.urls import url#Importamos las Funciones "url"
from django.urls import path, include#Importamos las Funciones de "Path" & "Include"
from Base_User import views #Importamos las Vistas(views.py) que se encuentran en App_Base

urlpatterns=[
path('CrearUsuarios/', views.CrearUsuario.as_view()),

]