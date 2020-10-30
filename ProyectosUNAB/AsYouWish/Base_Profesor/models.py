from django.db import models

# Create your models here.
product_Genero= [('Hombre','Hombre'),('Mujer','Mujer'),]

class Profesor(models.Model):
    RUTprof=models.CharField(max_length=13)
    NombreProf=models.CharField(max_length=30)
    GeneroProf=models.CharField(max_length=6,choices=product_Genero)
    LocalPerteneciente=models.CharField(max_length=50)
    ClaseProfesor=models.CharField(max_length=50)
    EmailProf=models.EmailField(blank=True, null=True)
    NtelefonoProf=models.CharField(max_length=20,blank=True, null=True)