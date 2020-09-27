from django.db import models

# Create your models here.
class Profesor(models.Model):
    RUTprof=models.CharField(max_length=13)
    NombreProf=models.CharField(max_length=30)
    GeneroProf=models.CharField(max_length=6)
    LocalPerteneciente=models.CharField(max_length=50)
    ClaseProfesor=models.CharField(max_length=50)
    EmailProf=models.EmailField(blank=True, null=True)
    NtelefonoProf=models.IntegerField(blank=True, null=True)