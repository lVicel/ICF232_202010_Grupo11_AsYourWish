from django.conf.urls import url#Importamos las Funciones "url"
from django.urls import path, include#Importamos las Funciones de "Path" & "Include"
from Base_Clase import views #Importamos las Vistas(views.py) que se encuentran en Base_Alumno

urlpatterns=[
url('Listado_Clase/', views.Lista_PagClase),#Creamos un nuevo URL para nuestra Pagina
url('Registrar_Clase/', views.Registrar_PagClase),#URL con el Formulario de Registro
path('Modificar_Clase/<id>/', views.Modificar_PagClase),
path('Eliminar_Clase/<id>/', views.Eliminar_PagClase),
url('buscar_Clase/', views.BuscarClase),
]