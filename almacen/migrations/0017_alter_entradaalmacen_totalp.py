# Generated by Django 4.2.1 on 2023-06-02 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0016_alter_entradaalmacen_totalp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradaalmacen',
            name='totalP',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
