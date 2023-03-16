# Generated by Django 4.0.5 on 2023-03-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendientes', '0009_alter_pendientes_area_alter_pendientes_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendientes',
            name='Area',
            field=models.CharField(choices=[('SubAcademica', 'SubAcademica'), ('SubPlaneacion', 'SubPlaneacion'), ('SubAdministrativa', 'SubAdministrativa')], max_length=30, verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='pendientes',
            name='estado',
            field=models.CharField(choices=[('Finalizada', 'Finalizada'), ('En Proceso', 'En Proceso'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=25, verbose_name='Estado'),
        ),
    ]
