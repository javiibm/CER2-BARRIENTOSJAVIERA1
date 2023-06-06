# Generated by Django 3.2.9 on 2023-06-06 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunicado',
            name='nivel',
            field=models.CharField(choices=[('GEN', 'General'), ('PRE', 'Ciclo Preescolar'), ('BAS', 'Ciclo Básico'), ('MED', 'Ciclo Medio')], default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='comunicado',
            name='detalle',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='comunicado',
            name='titulo',
            field=models.TextField(max_length=50),
        ),
    ]
