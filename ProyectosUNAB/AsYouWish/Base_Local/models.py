from django.db import models

# Create your models here.
class Local(models.Model):
    Anno=models.IntegerField()
    Mes=models.CharField(max_length=11)
    NombreLocal=models.CharField(max_length=20)
    PromedioIngresos=models.IntegerField()
    TasaAsist=models.IntegerField()
    TotalAlumnos=models.IntegerField()
    NuevosAlumnos=models.IntegerField()