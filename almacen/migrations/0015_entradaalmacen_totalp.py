# Generated by Django 4.2.1 on 2023-06-02 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0014_remove_entradaalmacen_resultado'),
    ]

    operations = [
        migrations.AddField(
            model_name='entradaalmacen',
            name='totalP',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
