# Generated by Django 4.2.1 on 2023-05-22 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0010_entradaalmacen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='almacen',
            name='nombreProducto',
        ),
    ]
