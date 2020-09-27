from django.db import models

# Create your models here.
class Klase(models.Model):
    NombreClas=models.CharField(max_length=50)
    ClassInicio=models.TimeField('%H:%M')
    ClassTermino=models.TimeField('%H:%M')
    Profesor=models.CharField(max_length=50)
    AsistHombres=models.IntegerField()
    AsistMujeres=models.IntegerField()
    AsistTotales=models.IntegerField()
    AsistPorcentaje=models.IntegerField()
    PaseVencidos=models.IntegerField()

