from django.db import models

# Create your models here.
Mes_Select= [('Enero','Enero'),('Febrero','Febrero'),('Marzo','Marzo'),('Abril','Abril'),('Mayo','Mayo'),('Junio','Junio'),('Julio','Julio'),('Agosto','Agosto'),('Septiembre','Septiembre'),('Octubre','Octube'),('Noviembre','Noviembre'),('Diciembre','Diciembre'),]

class EstadoMensual(models.Model):
    Anno=models.PositiveIntegerField()
    Mes=models.CharField(max_length=15, choices=Mes_Select)
    #PromedioIngreso=models.PositiveIntegerField()
    TotalIngresos=models.PositiveIntegerField()