# Generated by Django 4.2.1 on 2023-05-12 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('sku', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fkproveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.proveedor')),
            ],
        ),
    ]
