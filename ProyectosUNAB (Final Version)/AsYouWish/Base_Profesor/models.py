from django.db import models

# Create your models here.
product_Genero= [('Hombre','Hombre'),('Mujer','Mujer'),]
Locales_Disponibles=[('Casa Matriz','Casa Matriz'),('Bellavista','Bellavista'),('Providencia','Providencia'),('La Florida','La Florida'),]


class Profesor(models.Model):
    RUTprof=models.CharField(max_length=13, unique=True)
    NombreProf=models.CharField(max_length=30)
    GeneroProf=models.CharField(max_length=6,choices=product_Genero)
    LocalPerteneciente=models.CharField(max_length=50, choices=Locales_Disponibles)
    ClaseProfesor=models.CharField(max_length=50)
    EmailProf=models.EmailField(blank=True, null=True)
    NtelefonoProf=models.CharField(max_length=20,blank=True, null=True)