from django.conf.urls import url#Importamos las Funciones "url"
from django.urls import path, include#Importamos las Funciones de "Path" & "Include"
from Base_Local import views #Importamos las Vistas(views.py) que se encuentran en App_Base

urlpatterns=[
url('Listado_Academias/', views.Academias_AsYouWish),#Inicio_Locales.html
url('Estado_CasaMatriz/',views.Estado_CasaMatriz),
url('Estado_Bellavista/',views.Estado_Bellavista),
url('Estado_Providencia/',views.Estado_Providencia),
url('Estado_LaFlorida/',views.Estado_LaFlorida),
]