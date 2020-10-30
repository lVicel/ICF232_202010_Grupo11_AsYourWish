from django.db import models

# Create your models here.
#Creación de clase User para poder ser listado.
class User(models.Model):
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=254)
    rut=models.CharField(max_length=12)