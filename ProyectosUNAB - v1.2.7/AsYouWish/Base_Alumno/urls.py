from django.conf.urls import url#Importamos las Funciones "url"
from django.urls import path, include#Importamos las Funciones de "Path" & "Include"
from Base_Alumno import views #Importamos las Vistas(views.py) que se encuentran en Base_Alumno

urlpatterns=[
url('Listado_Alumnos/', views.Lista_Alumnos),#Alumnos/Lista_Alumno.html
url('Registrar_Alumno/', views.Registrar_Alumnos),#Alumnos/Registrar_Alumno.html
path('Modificar_Alumno/<id>/', views.Modificar_Alumnos),#Alumnos/Modificar_Alumno.html
path('Eliminar_Alumno/<id>/', views.Eliminar_Alumnos),#Path para Eliminar

#Participantes
path('Listado_Clases_Locales/<Nombre>/', views.ClasesLocales),

#Pagos
path('Listado_Pagos/<id>/', views.Pagos_Alumno),
path('Registrar_Pago/<id>/', views.Registrar_Pago),
path('Eliminar_Pago/<id>/', views.Eliminar_Pagos),
]