from django.conf.urls import url#Importamos las Funciones "url"
from django.urls import path, include#Importamos las Funciones de "Path" & "Include"
from Base_Evento import views #Importamos las Vistas(views.py) que se encuentran en Base_Alumno

urlpatterns=[
url('Listado_Evento/', views.Lista_PagEvento),#Creamos un nuevo URL para nuestra Pagina
url('Registrar_Evento/', views.Registrar_PagEvento),#URL con el Formulario de Registro
path('Modificar_Evento/<id>/', views.Modificar_PagEvento),
path('Eliminar_Evento/<id>/', views.Eliminar_PagEvento),
url('Buscar_Event/', views.BuscarEventos),
]