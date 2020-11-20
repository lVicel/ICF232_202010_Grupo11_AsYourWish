from django.db import models

# Create your models here.
class EstadoMensual(models.Model):
    Global=models.CharField(max_length=20, default='Global')
    Anno=models.IntegerField()
    Mes=models.CharField(max_length=11)
    PromedioIngreso=models.IntegerField()
    PromedioAsist=models.IntegerField()
    AlumnosNuevos=models.IntegerField()