# Generated by Django 3.1.1 on 2020-09-22 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_Local', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='Anno',
            field=models.IntegerField(default=2020),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='local',
            name='Mes',
            field=models.CharField(default='Enero', max_length=11),
            preserve_default=False,
        ),
    ]
