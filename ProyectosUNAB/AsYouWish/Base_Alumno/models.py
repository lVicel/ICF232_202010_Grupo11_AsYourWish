from django.db import models
import datetime

# Create your models here.
product_Genero= [('Hombre','Hombre'),('Mujer','Mujer'),]

class Alumno(models.Model):
    RUT=models.CharField(max_length=13)
    Nombre=models.CharField(max_length=30)
    Genero=models.CharField(max_length=6,choices=product_Genero)
    Nacimiento=models.DateField()
    Profesion=models.CharField(max_length=50)
    DirPersonal=models.CharField(max_length=50)
    DirLaboral=models.CharField(max_length=50)
    Email=models.EmailField(blank=True, null=True)
    Ntelefono=models.CharField(max_length=20,blank=True, null=True)

class PagosAlumno(models.Model):
    id_Alumno=models.IntegerField()
    RUT=models.CharField(max_length=13)
    Nombre=models.CharField(max_length=30)
    FechaIngresos=models.DateField(default=datetime.date.today)
    Local=models.CharField(max_length=30)
    ClasePagada=models.CharField(max_length=30)
    Horario_Inicio=models.TimeField('%H:%M')
    Horario_Termino=models.TimeField('%H:%M')
    IngresoAlumnno=models.IntegerField()
    MetodoPago=models.CharField(max_length=30)


class Participante(models.Model):
    Nombre=models.CharField(max_length=30)
    Clase_Perteneciente=models.CharField(max_length=30)
    Local=models.CharField(max_length=30)
    Code_Clase=models.IntegerField()
    Horario_Inicio=models.TimeField('%H:%M')
    Horario_Termino=models.TimeField('%H:%M')
    AsistPorcentaje=models.IntegerField()
    AsistTotales=models.IntegerField()



class ParticipantesEvent(models.Model):
    EventInscrito=models.CharField(max_length=30)
    ID_Event=models.IntegerField()
    NombreParticipante=models.CharField(max_length=30)
    Escena=models.CharField(max_length=30)




#Como crear una Base de DAtos Db.sqlite3: (Asegurate que se configuraron en Setting la App)
#1° Asegurate que los Atributos estan bien definidos
#2° Revisa que todo esta en orden con CMD escribiendo: python manage.py check
#3° Para crear la Base de Datos sqlite3 escribe: python manage.py makemigrations (De esta forma lo creara)
#4° Ahora hay que generar el Codigo, escribe: python manage.py sqlmigrate Base_Alumno (Nombre App) N°Migracion (0001 por 0001_initial.py en este caso)
#[Deberia crearse las tablas CREATE TABLE]
#5° Ahora ingresa las tablas en la B.D: python manage.py migrate (Con DB Browse podemos ver la B.D)
