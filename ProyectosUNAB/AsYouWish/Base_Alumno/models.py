from django.db import models

# Create your models here.
class Alumno(models.Model):
    RUT=models.CharField(max_length=13)
    Nombre=models.CharField(max_length=30)
    Genero=models.CharField(max_length=6)
    Nacimiento=models.DateField()
    Profesion=models.CharField(max_length=50)
    DirPersonal=models.CharField(max_length=50)
    DirLaboral=models.CharField(max_length=50)
    Asistencias=models.IntegerField()
    Email=models.EmailField(blank=True, null=True)
    Ntelefono=models.IntegerField(blank=True, null=True)




#Como crear una Base de DAtos Db.sqlite3: (Asegurate que se configuraron en Setting la App)
#1° Asegurate que los Atributos estan bien definidos
#2° Revisa que todo esta en orden con CMD escribiendo: python manage.py check
#3° Para crear la Base de Datos sqlite3 escribe: python manage.py makemigrations (De esta forma lo creara)
#4° Ahora hay que generar el Codigo, escribe: python manage.py sqlmigrate Base_Alumno (Nombre App) N°Migracion (0001 por 0001_initial.py en este caso)
#[Deberia crearse las tablas CREATE TABLE]
#5° Ahora ingresa las tablas en la B.D: python manage.py migrate (Con DB Browse podemos ver la B.D)
