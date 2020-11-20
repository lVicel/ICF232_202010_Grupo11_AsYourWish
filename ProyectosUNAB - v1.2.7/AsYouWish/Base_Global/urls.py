from django.conf.urls import url#Importamos las Funciones "url"
from django.urls import path, include#Importamos las Funciones de "Path" & "Include"
from Base_Global import views #Importamos las Vistas(views.py) que se encuentran en Base_Alumno

urlpatterns=[
url('Registro_Global/', views.Registro_Mensual),#Creamos un nuevo URL para nuestra Pagina
]