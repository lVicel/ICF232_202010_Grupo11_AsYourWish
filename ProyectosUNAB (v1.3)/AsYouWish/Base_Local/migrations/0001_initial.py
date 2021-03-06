# Generated by Django 3.1.1 on 2020-11-21 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Local', models.CharField(choices=[('Casa Matriz', 'Casa Matriz'), ('Bellavista', 'Bellavista'), ('Providencia', 'Providencia'), ('La Florida', 'La Florida')], max_length=30)),
                ('Anno', models.PositiveIntegerField()),
                ('Mes', models.CharField(choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octube'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], max_length=15)),
                ('TotalIngresos', models.PositiveIntegerField()),
            ],
        ),
    ]
