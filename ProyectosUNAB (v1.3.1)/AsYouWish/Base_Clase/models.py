from django.db import models
import random, string


def random_string():
        return random.randint(0, 999)


# Create your models here.
Dias_Semana= [('Lunes','Lunes'),('Martes','Martes'),('Miercoles','Miercoles'),('Jueves','Jueves'),('Viernes','Viernes'),('Sabado','Sabado'),('Domingo','Domingo'),]
Locales_Disponibles=[('Casa Matriz','Casa Matriz'),('Bellavista','Bellavista'),('Providencia','Providencia'),('La Florida','La Florida'),]

class Klase(models.Model):
    NombreClas=models.CharField(max_length=50)
    Local=models.CharField(max_length=30, choices=Locales_Disponibles)
    Dia=models.CharField(max_length=10, choices=Dias_Semana)
    ClassInicio=models.TimeField('%H:%M')
    ClassTermino=models.TimeField('%H:%M')
    Profesor=models.CharField(max_length=50)
    AsistHombres=models.PositiveIntegerField(default=0)
    AsistMujeres=models.PositiveIntegerField(default=0)
    AsistTotales=models.PositiveIntegerField(default=0)