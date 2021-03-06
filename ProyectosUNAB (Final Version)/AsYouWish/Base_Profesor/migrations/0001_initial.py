# Generated by Django 3.1.1 on 2020-11-21 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RUTprof', models.CharField(max_length=13, unique=True)),
                ('NombreProf', models.CharField(max_length=30)),
                ('GeneroProf', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=6)),
                ('LocalPerteneciente', models.CharField(choices=[('Casa Matriz', 'Casa Matriz'), ('Bellavista', 'Bellavista'), ('Providencia', 'Providencia'), ('La Florida', 'La Florida')], max_length=50)),
                ('ClaseProfesor', models.CharField(max_length=50)),
                ('EmailProf', models.EmailField(blank=True, max_length=254, null=True)),
                ('NtelefonoProf', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
