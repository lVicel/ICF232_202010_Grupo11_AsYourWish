from django.db import models

# Create your models here.
Locales_Disponibles=[('Casa Matriz','Casa Matriz'),('Bellavista','Bellavista'),('Providencia','Providencia'),('La Florida','La Florida'),]
Mes_Select= [('Enero','Enero'),('Febrero','Febrero'),('Marzo','Marzo'),('Abril','Abril'),('Mayo','Mayo'),('Junio','Junio'),('Julio','Julio'),('Agosto','Agosto'),('Septiembre','Septiembre'),('Octubre','Octube'),('Noviembre','Noviembre'),('Diciembre','Diciembre'),]

class Local(models.Model):
    Local=models.CharField(max_length=30, choices=Locales_Disponibles)
    Anno=models.PositiveIntegerField()
    Mes=models.CharField(max_length=15,choices=Mes_Select)
    TotalIngresos=models.PositiveIntegerField()