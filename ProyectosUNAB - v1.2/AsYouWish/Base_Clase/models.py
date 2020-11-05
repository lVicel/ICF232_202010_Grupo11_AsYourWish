from django.db import models
import random, string


def random_string():
        return random.randint(0, 999)


# Create your models here.
class Klase(models.Model):
    Code_Clase=models.IntegerField(default=random_string)
    NombreClas=models.CharField(max_length=50)
    Local=models.CharField(max_length=30)
    ClassInicio=models.TimeField('%H:%M')
    ClassTermino=models.TimeField('%H:%M')
    Profesor=models.CharField(max_length=50)
    AsistHombres=models.IntegerField()
    AsistMujeres=models.IntegerField()
    AsistTotales=models.IntegerField()
    AsistPorcentaje=models.IntegerField()
    PaseVencidos=models.IntegerField()