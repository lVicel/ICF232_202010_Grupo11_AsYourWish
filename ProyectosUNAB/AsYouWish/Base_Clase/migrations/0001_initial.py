# Generated by Django 3.1.1 on 2020-09-19 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreClas', models.CharField(max_length=50)),
                ('Profesor', models.CharField(max_length=50)),
                ('AsistHombres', models.IntegerField()),
                ('AsistMujeres', models.IntegerField()),
                ('AsistTotales', models.IntegerField()),
                ('AsitPorcentaje', models.IntegerField()),
                ('PaseVencidos', models.IntegerField()),
            ],
        ),
    ]
