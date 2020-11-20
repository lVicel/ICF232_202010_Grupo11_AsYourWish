from django.db import models
# Create your models here.
LUGARES = (
    ("1", "Seleccione su residencia correspondiente"),
    ("2", "Casa Matriz"),
    ("3", "Bellavista"),
    ("4", "La Florida"),
    ("5", "Providencia"),
)
#Creación de clase User para poder ser listado.
class Usuario(models.Model):
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=254)
    rut=models.CharField(max_length=12)
    residencia=models.CharField(max_length = 1,choices=LUGARES, default="1")

#    class Meta:
#        permissions = (
 #           ("registrar_asistencias_alumnos", "Permite registrar las asistencias de los alumnos"),
#          ("modificar_asistencias_alumnos", "Permite modificar las asistencias de los alumnos"),
 #           ("eliminar_asistencias_alumnos", "Permite eliminar las asistencias de los alumnos"),

  #      )
# Los 3 Usuarios o Grupos eran los Siguientes:
# Basico --> Solo podra ser capaz de registrar las Asistencias de Alumnos
#
# Anfitrion-->Solo podra visualizar los Datos de las Tablas, pero NO capaz de Registrar, Modificar o Eliminar algun tipo de Objeto o Dato
#
# Director-->Ademas de visualizar los Datos de las Tablas, este tambien podra registrar, Modifcar, o Eliminar algun tipo de Objeto o Dato.
