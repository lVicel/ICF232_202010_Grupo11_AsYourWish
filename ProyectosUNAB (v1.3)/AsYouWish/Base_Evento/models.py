from django.db import models

# Create your models here.
Locales_Disponibles=[('Casa Matriz','Casa Matriz'),('Bellavista','Bellavista'),('Providencia','Providencia'),('La Florida','La Florida'),]

class Evento(models.Model):
    NombreEvent=models.CharField(max_length=30)
    FechaEvent=models.DateField()
    EventInicio=models.TimeField('%H:%M')
    EventTermino=models.TimeField('%H:%M')
    LocalAdmin=models.CharField(max_length=30, choices=Locales_Disponibles)
    Direccion=models.CharField(max_length=50)
