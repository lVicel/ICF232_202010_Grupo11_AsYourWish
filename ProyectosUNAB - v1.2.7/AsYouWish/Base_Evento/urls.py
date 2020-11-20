from django.conf.urls import url#Importamos las Funciones "url"
from django.urls import path, include#Importamos las Funciones de "Path" & "Include"
from Base_Evento import views #Importamos las Vistas(views.py) que se encuentran en Base_Alumno

urlpatterns=[
url('Listado_Eventos/', views.Lista_Eventos),#Eventos/Lista_Evento.html
url('Registrar_Evento/', views.Registrar_Eventos),#Eventos/Registrar_Evento.html
path('Modificar_Evento/<id>/', views.Modificar_Eventos),#Eventos/Modicificar_Evento.html
path('Eliminar_Evento/<id>/', views.Eliminar_Eventos),#Path para Eliminar

#Participantes Evento
path('Participantes_Evento/<id>/', views.Participantes_Evento),
path('Registrar_ParticipanteEvent/<id>/', views.Registrar_ParticipanteEvent),
path('Eliminar_ParticipanteEvent/<id>/',views.Eliminar_ParticipanteEvent),
]