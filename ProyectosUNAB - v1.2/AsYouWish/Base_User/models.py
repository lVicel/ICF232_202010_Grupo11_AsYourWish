from django.db import models
# Create your models here.
LUGARES = (
    ("1", "Seleccione su residencia correspondiente"),
    ("2", "Casa Matriz"),
    ("3", "Bellavista"),
    ("4", "La Florida"),
    ("5", "Providencia"),
)
#Creación de clase User para poder ser listado.
class Usuario(models.Model):
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=254)
    rut=models.CharField(max_length=12)
    residencia=models.CharField(max_length = 1,choices=LUGARES, default="1")
