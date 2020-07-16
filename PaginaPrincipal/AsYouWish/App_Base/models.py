from django.db import models
# Create your models here.

#Tabla de Clase Alumno
class Alumno(models.Model):#models.Model-->Trabajaremos en estilo Model
	RUT=models.CharField(max_length=13)#"max_lenght"=Cantidad Max. de caracteres
	Nombre=models.CharField(max_length=30)
	Email=models.EmailField(blank=True,null=True)#Nos permite dejarlo en Blanco

	def __str__(self): #OJO: son 2 "_"
		return self.Nombre