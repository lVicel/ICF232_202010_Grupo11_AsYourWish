from django.conf.urls import url#Importamos las Funciones "url"
from django.urls import path, include#Importamos las Funciones de "Path" & "Include"
from Base_Profesor import views #Importamos las Vistas(views.py) que se encuentran en Base_Alumno

urlpatterns=[
url('Listado_Profesor/', views.Lista_PagProfe),#Creamos un nuevo URL para nuestra Pagina
url('Registrar_Profesor/', views.Registrar_PagProfe),#URL con el Formulario de Registro
path('Modificar_Profesor/<id>/', views.Modificar_PagProfe),
path('Eliminar_Profesor/<id>/', views.Eliminar_PagProfe),
url('buscar_Prof/', views.BuscarProfesor),
]