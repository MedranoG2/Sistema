from django.contrib import admin
from .models import Proveedor, Producto, Departamento, Empleado, Almacen, EntradaAlmacen, Pedido
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Departamento)
admin.site.register(Empleado)
admin.site.register(Almacen)
admin.site.register(EntradaAlmacen)
admin.site.register(Pedido)
