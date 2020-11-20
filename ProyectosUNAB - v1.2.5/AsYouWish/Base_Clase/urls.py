from django.conf.urls import url#Importamos las Funciones "url"
from django.urls import path, include#Importamos las Funciones de "Path" & "Include"
from Base_Clase import views #Importamos las Vistas(views.py) que se encuentran en Base_Alumno

urlpatterns=[
#Clases
url('Listado_Clases/', views.Lista_Clases),#Clases/Lisa_Clase.html
url('Registrar_Clase/', views.Registrar_Clases),#Clases/Registrar_Clase.html
path('Modificar_Clase/<id>/', views.Modificar_Clases),
path('Eliminar_Clase/<id>/', views.Eliminar_PagClase),

#Participantes
path('Participantes/<id>/',views.Participantes_Clase),
path('Registrar_Participante/<id>/', views.Registrar_Participante),
path('Eliminar_Participante/<id>/', views.Eliminar_Participante),


#Asistencias
url('Inicio_Asistencias/',views.PagInicio_Asistencias),
path('Lista_Asistencias/<id>/',views.Lista_Asistencia),
]