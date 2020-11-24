from django.conf.urls import url#Importamos las Funciones "url"
from django.urls import path, include#Importamos las Funciones de "Path" & "Include"
from Base_User import views

urlpatterns=[
url('CrearUsuarios/', views.CrearUsuario),
url('Listado_Usario/', views.Lista_Usuarios), #url de listado de usuarios
path('Eliminar_Usuario/<id>/', views.EliminarUsuario)
]