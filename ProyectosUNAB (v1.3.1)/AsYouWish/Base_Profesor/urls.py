from django.conf.urls import url#Importamos las Funciones "url"
from django.urls import path, include#Importamos las Funciones de "Path" & "Include"
from Base_Profesor import views #Importamos las Vistas(views.py) que se encuentran en Base_Alumno

urlpatterns=[
url('Listado_Profesores/', views.Lista_Profesores),#Lista_Profesor.html
url('Registrar_Profesor/', views.Registrar_Profesores),#Modificar_Profesor.html
path('Modificar_Profesor/<id>/', views.Modificar_Profesores),#Modificar_Profesor.html
path('Eliminar_Profesor/<id>/', views.Eliminar_Profesores),#Path para Eliminar
]