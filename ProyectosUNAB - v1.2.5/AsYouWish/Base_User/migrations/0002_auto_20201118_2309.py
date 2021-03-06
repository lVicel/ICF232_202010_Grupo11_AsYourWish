# Generated by Django 3.0.6 on 2020-11-19 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('rut', models.CharField(max_length=12)),
                ('residencia', models.CharField(choices=[('1', 'Seleccione su residencia correspondiente'), ('2', 'Casa Matriz'), ('3', 'Bellavista'), ('4', 'La Florida'), ('5', 'Providencia')], default='1', max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
