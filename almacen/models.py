from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from django.core.exceptions import ValidationError


# Create your models here.


class Proveedor(models.Model):
    idProveedor = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return self.idProveedor


class Producto(models.Model):
    sku = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    codigoBarras = models.CharField(max_length=70)
    fkproveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    idDepartamento = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.idDepartamento


class Empleado(models.Model):
    idEmpleado = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fkdepartamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.idEmpleado


class Almacen(models.Model):
    idAlmacen = models.AutoField(primary_key=True)
    Fksku = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.idAlmacen


class EntradaAlmacen(models.Model):
    idEntradaAlmacen = models.AutoField(primary_key=True)
    Fksku = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fechaEntrada = models.DateField()
    cantidad = models.IntegerField()

    def valorTotal(self):
        return self.cantidad * self.Fksku.precio

    def __str__(self):
        return str(self.idEntradaAlmacen)

    def save(self, *args, **kwargs):
        super(EntradaAlmacen, self).save(*args, **kwargs)

        # Actualizar la cantidad en Almacen
        almacen = Almacen.objects.get(Fksku=self.Fksku)
        almacen.cantidad += int(self.cantidad)
        almacen.save()


class Pedido(models.Model):

    idPedido = models.AutoField(primary_key=True)
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    Fksku = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fechaPedido = models.DateField()
    cantidad = models.IntegerField()

    def valorTotal(self):
        return self.cantidad * self.Fksku.precio

    def _str_(self):
        return str(self.idPedido)

    def save(self, *args, **kwargs):
        # Verificar si la cantidad en Almacen es suficiente
        almacenes = Almacen.objects.filter(Fksku=self.Fksku)
        if almacenes.exists():
            almacen = almacenes.first()
            if int(self.cantidad) > almacen.cantidad:
                raise ValidationError(
                    "No hay suficiente cantidad del producto :)")

            super(Pedido, self).save(*args, **kwargs)

            almacen.cantidad -= int(self.cantidad)
            if almacen.cantidad < 0:
                almacen.cantidad = 0
                almacen.save()
                raise ValidationError("No quedan productos disponibles.")
            else:
                almacen.save()
        else:
            raise ValidationError(
                "No se encontró el objeto Almacen asociado al producto.")
