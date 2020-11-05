from django.db import models

# Create your models here.
class Evento(models.Model):
    NombreEvent=models.CharField(max_length=30)
    FechaEvent=models.DateField()
    EventInicio=models.TimeField('%H:%M')
    EventTermino=models.TimeField('%H:%M')
    LocalAdmin=models.CharField(max_length=50)
    Direccion=models.CharField(max_length=50)
