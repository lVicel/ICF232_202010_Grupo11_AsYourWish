from django.db import models

# Create your models here.
#Creación de clase User para poder ser listado.
class Usuario(models.Model):
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=254)
    rut=models.CharField(max_length=12)
    Residencia_Choices= (
        ("1", "Residencia1"),
        ("2", "Residencia2"),
        ("3", "Residencia3"),
        ("4", "Residencia4"),
        ("5", "Residencia5"),
    )
    residencia=models.CharField(max_length=20,choices=Residencia_Choices,default='1')