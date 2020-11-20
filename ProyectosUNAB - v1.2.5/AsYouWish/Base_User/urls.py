from django.conf.urls import url#Importamos las Funciones "url"
from django.urls import path, include#Importamos las Funciones de "Path" & "Include"
from . import views

urlpatterns=[
url('CrearUsuarios/', views.CrearUsuario),
url('Listado_Usario/', views.Lista_Usuarios), #url de listado de usuarios

#urls para asignar grupos de permisos
path('Asignar_Basico/<id>/', views.Asignar_Basico),
path('Asignar_Anfitrion/<id>/', views.Asignar_Anfitrion),
path('Asignar_Director/<id>/', views.Asignar_Director),

#urls para eliminar usuarios de grupos
path('Eliminar_Basico/<id>/', views.Eliminar_Basico),
path('Eliminar_Anfitrion/<id>/', views.Eliminar_Anfitrion),
path('Eliminar_Director/<id>/', views.Eliminar_Director),
#url para eliminar usuario
path('Eliminar_Usuario/<id>/', views.Eliminar_Usuarios)
]