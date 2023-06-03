from django.shortcuts import render, redirect
from .models import Proveedor, Producto, Departamento, Empleado, Almacen, EntradaAlmacen, Pedido
from django.contrib import messages
from .forms import ProductoForm, ProveedorForm, DepartamentoForm, EmpladoForm, AlmacenForm, EntradaAlmacenForm, PedidoForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import View
from django.db.models import Q


# Create your views here.


def inicio(request):
    return render(request, "inicio.html")


def registrarProveedor(request):
    form = ProveedorForm()
    proveedores = Proveedor.objects.all()

    if request.method == 'POST':
        buscar = request.POST.get('buscar')

        if buscar:
            proveedores = proveedores.filter(
                Q(nombre__icontains=buscar) |
                Q(idProveedor__icontains=buscar)).distinct()

    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro Exitoso!')
            return redirect('registrar_proveedor')

    context = {
        'form': form,
        'proveedores': proveedores
    }

    return render(request, 'registroProveedor.html', context)


def edicionProveedor(request, codigo):
    proveedores = get_object_or_404(Proveedor, idProveedor=codigo)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedores)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor actualizado correctamente.')
            return redirect('registrar_proveedor')
    else:
        form = ProveedorForm(instance=proveedores)
    return render(request, 'ActualizarProveedor.html', {'form': form, 'proveedores': proveedores})


def actualizar_proveedor(request, codigo):
    proveedores = get_object_or_404(Proveedor, idProveedor=codigo)

    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedores)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor actualizado correctamente.')
            # Redirecciona a la página de inicio o a la página relevante después de guardar
            return redirect('registrar_proveedor')
    else:
        form = ProveedorForm(instance=proveedores)

    return render(request, 'ActualizarProveedor.html', {'form': form, 'proveedores': proveedores})


def eliminarProveedor(request, codigo):
    proveedores = Proveedor.objects.get(idProveedor=codigo)
    proveedores.delete()
    messages.success(request, 'Eliminado!')
    return redirect('registrar_proveedor')


def registrarProducto(request):
    form = ProductoForm()
    proveedores = Proveedor.objects.all()
    productos = Producto.objects.all()

    if request.method == 'POST':
        buscar = request.POST.get('buscar')

        if buscar:
            productos = productos.filter(
                Q(nombre__icontains=buscar) |
                Q(sku__icontains=buscar)).distinct()

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro Exitoso!')
            return redirect('registrar_producto')

    context = {
        'form': form,
        'proveedores': proveedores,
        'productos': productos
    }

    return render(request, 'registroProducto.html', context)


def edicionProducto(request, codigo):
    producto = get_object_or_404(Producto, sku=codigo)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente!')
            return redirect('registrar_producto')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'actualizarProducto.html', {'form': form, 'producto': producto})


def eliminarProducto(request, codigo):
    producto = Producto.objects.get(sku=codigo)
    producto.delete()
    messages.success(request, 'Eliminado!')
    return redirect('registrar_producto')


def actualizarProducto(request, codigo):
    producto = get_object_or_404(Producto, sku=codigo)
    form = ProductoForm(instance=producto)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente!')
            return redirect('registrar_producto')

    return render(request, 'actualizarProducto.html', {'form': form, 'producto': producto})


def registrarDepartamento(request):
    form = DepartamentoForm()
    departamentos = Departamento.objects.all

    if request.method == 'POST':

        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro Exitoso!')
            return redirect('registroDepartamento')

    return render(request, 'registroDepartamento.html', {'form': form, 'departamentos': departamentos})


def edicionDepartamento(request, codigo):
    departamentos = get_object_or_404(Departamento, idDepartamento=codigo)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamentos)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Departamento actualizado correctamente.')
            return redirect('registroDepartamento')
    else:
        form = DepartamentoForm(instance=departamentos)
    return render(request, 'actualizarDepartamento.html', {'form': form, 'departamentos': departamentos})


def actualizarDepartamento(request, codigo):
    departamentos = get_object_or_404(Departamento, idDepartamento=codigo)
    form = DepartamentoForm(instance=departamentos)

    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamentos)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departamento actualizado exitosamente!')
            return redirect('registroDepartamento')

    return render(request, 'actualizarDepartamento.html', {'form': form, 'departamentos': departamentos})


def eliminarDepartamento(request, codigo):
    departamentos = Departamento.objects.get(idDepartamento=codigo)
    departamentos.delete()
    messages.success(request, 'Eliminado!')
    return redirect('registroDepartamento')


def registrarEmpleado(request):
    form = EmpladoForm()
    departamentos = Departamento.objects.all()
    empleados = Empleado.objects.all()

    if request.method == 'POST':
        buscar = request.POST.get('buscar')

        if buscar:
            empleados = empleados.filter(
                Q(nombre__icontains=buscar) |
                Q(idEmpleado__icontains=buscar)).distinct()

    if request.method == 'POST':
        form = EmpladoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro Exitoso!')
            return redirect('registroEmpleado')

    context = {
        'form': form,
        'empleados': empleados,
        'departamentos': departamentos
    }
    return render(request, 'registroEmpleado.html', context)


def actualizarEmpleado(request, codigo):
    empleados = get_object_or_404(Empleado, idEmpleado=codigo)
    form = EmpladoForm(instance=empleados)

    if request.method == 'POST':
        form = EmpladoForm(request.POST, instance=empleados)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado actualizado exitosamente!')
            return redirect('registroEmpleado')

    return render(request, 'actualizarEmpleado.html', {'form': form, 'empleados': empleados})


def edicionEmpleado(request, codigo):
    empleados = get_object_or_404(Empleado, idEmpleado=codigo)

    if request.method == 'POST':
        form = EmpladoForm(request.POST, instance=empleados)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado actualizado exitosamente!')
            return redirect('registroEmpleado')
    else:
        form = EmpladoForm(instance=empleados)

    return render(request, 'actualizarEmpleado.html', {'form': form, 'empleados': empleados})


def eliminarEmpleado(request, codigo):
    empleados = Empleado.objects.get(idEmpleado=codigo)
    empleados.delete()
    messages.success(request, 'Eliminado!')
    return redirect('registroEmpleado')


def registrarAlmacen(request):
    form = AlmacenForm()
    almacenes = Almacen.objects.all()

    if request.method == 'POST':
        buscar = request.POST.get('buscar')

        if buscar:
            almacenes = almacenes.filter(
                Q(idAlmacen__icontains=buscar) |
                Q(Fksku_id__nombre__icontains=buscar) |
                Q(Fksku_id__sku__icontains=buscar)).distinct()

    if request.method == 'POST':
        form = AlmacenForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro Exitoso!')
            return redirect('registrar_almacen')
    context = {
        'form': form,
        'almacenes': almacenes
    }

    return render(request, 'registroAlmacen.html', context)


def edicionAlmacen(request, codigo):
    almacenes = get_object_or_404(Almacen, idAlmacen=codigo)

    if request.method == 'POST':
        form = AlmacenForm(request.POST, instance=almacenes)
        if form.is_valid():
            form.save()
            messages.success(request, 'Almacen actualizado exitosamente!')
            return redirect('registro_almacen')
    else:
        form = AlmacenForm(instance=almacenes)

    return render(request, 'actualizarAlmacen.html', {'form': form, 'almacenes': almacenes})


def actualizarAlmacen(request, codigo):
    almacen = get_object_or_404(Almacen, idAlmacen=codigo)

    if request.method == 'POST':
        cantidad = request.POST.get('cantidad')
        almacen.cantidad = cantidad
        almacen.save()
        messages.success(request, 'Almacen actualizado exitosamente!')
        return redirect('registrar_almacen')


def eliminarAlmacen(request, codigo):
    almacenes = Almacen.objects.get(idAlmacen=codigo)
    almacenes.delete()
    messages.success(request, 'Eliminado!')
    return redirect('registrar_almacen')


def registrarEntradaAlmacen(request):
    form = EntradaAlmacenForm()
    entradaAlmacenes = EntradaAlmacen.objects.all()

    if request.method == 'POST':
        buscar = request.POST.get('buscar')

        if buscar:
            entradaAlmacenes = entradaAlmacenes.filter(
                Q(idEntradaAlmacen__icontains=buscar) |
                Q(Fksku_id__nombre__icontains=buscar) |
                Q(Fksku_id__sku__icontains=buscar)).distinct()

    if request.method == 'POST':
        form = EntradaAlmacenForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro Exitoso!')
            return redirect('registrar_EntradaAlmacen')

    context = {
        'form': form,
        'entradaAlmacenes': entradaAlmacenes
    }

    return render(request, 'registroEntradaAlmacen.html', context)


def edicionEntradaAlmacen(request, codigo):
    entradaAlmacenes = get_object_or_404(
        EntradaAlmacen, idEntradaAlmacen=codigo)

    if request.method == 'POST':
        form = EntradaAlmacenForm(request.POST, instance=entradaAlmacenes)
        if form.is_valid():
            form.save()
            messages.success(request, 'Almacen actualizado exitosamente!')
            return redirect('registrar_EntradaAlmacen')
    else:
        form = EntradaAlmacenForm(instance=entradaAlmacenes)

    return render(request, 'actualizarEntradaAlmacen.html', {'form': form, 'entradaAlmacenes': entradaAlmacenes})


def actualizarEntradaAlmacen(request, codigo):
    entradaAlmacen = get_object_or_404(
        EntradaAlmacen, idEntradaAlmacen=codigo)

    if request.method == 'POST':
        fechaEntrada = request.POST.get('fechaEntrada')
        cantidad = request.POST.get('cantidad')
        entradaAlmacen.cantidad = cantidad
        entradaAlmacen.fechaEntrada = fechaEntrada
        entradaAlmacen.save()
        messages.success(
            request, 'Entrada de Almacen actualizado exitosamente!')
        return redirect('registrar_EntradaAlmacen')


def eliminarEntradaAlmacen(request, codigo):
    entradaAlmacenes = EntradaAlmacen.objects.get(idEntradaAlmacen=codigo)
    entradaAlmacenes.delete()
    messages.success(request, 'Eliminado!')
    return redirect('registrar_EntradaAlmacen')


def registrarPedido(request):
    form = PedidoForm()
    pedidos = Pedido.objects.all()

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro Exitoso!')
            return redirect('registrar_Pedido')

    return render(request, 'registroPedido.html', {'form': form, 'pedidos': pedidos})


def edicionPedido(request, codigo):
    pedidos = get_object_or_404(
        Pedido, idPedido=codigo)

    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedidos)
        if form.is_valid():
            form.save()
            messages.success(request, 'Almacen actualizado exitosamente!')
            return redirect('registrar_Pedido')
    else:
        form = PedidoForm(instance=pedidos)

    return render(request, 'actualizarPedido.html', {'form': form, 'pedidos': pedidos})


def actualizarPedido(request, codigo):
    pedidos = get_object_or_404(
        Pedido, idPedido=codigo)

    if request.method == 'POST':
        fechaPedido = request.POST.get('fechaPedido')
        cantidad = request.POST.get('cantidad')
        pedidos.cantidad = cantidad
        pedidos.fechaPedido = fechaPedido
        pedidos.save()
        messages.success(
            request, 'Entrada de Almacen actualizado exitosamente!')
        return redirect('registrar_Pedido')


def eliminarPedido(request, codigo):
    pedidos = Pedido.objects.get(idPedido=codigo)
    pedidos.delete()
    messages.success(request, 'Eliminado!')
    return redirect('registrar_Pedido')


def reportePedido(request):
    pedidos = Pedido.objects.all()
    return render(request, "reportePedido.html", {'pedidos': pedidos})


def reporteIngresos(request):
    entradaAlmacenes = EntradaAlmacen.objects.all()
    return render(request, "reporteIngresos.html", {'entradaAlmacenes': entradaAlmacenes})


class GenerarReporteView(View):
    def post(self, request):
        # Obtiene las fechas de inicio y fin del formulario
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        # Obtiene el nombre del producto y FKSku del formulario
        nombre_producto = request.POST.get('nombre_producto')
        fksku = request.POST.get('fksku')

        # Realiza la consulta a la base de datos para obtener los pedidos en el rango de fechas y con los criterios adicionales
        pedidos = Pedido.objects.filter(
            fechaPedido__range=[fecha_inicio, fecha_fin],
            Fksku__nombre__icontains=nombre_producto,
            Fksku__sku__icontains=fksku
        )

        # Renderiza el template del informe con los datos obtenidos
        return render(request, 'reportePedido.html', {'pedidos': pedidos})


class GenerarReporteIngresoView(View):
    def post(self, request):
        # Obtiene las fechas de inicio y fin del formulario
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        # Obtiene el nombre del producto y FKSku del formulario
        nombre_producto = request.POST.get('nombre_producto')
        fksku = request.POST.get('fksku')

        # Realiza la consulta a la base de datos para obtener los pedidos en el rango de fechas y con los criterios adicionales
        entradaAlmacenes = EntradaAlmacen.objects.filter(
            fechaEntrada__range=[fecha_inicio, fecha_fin],
            Fksku__nombre__icontains=nombre_producto,
            Fksku__sku__icontains=fksku
        )

        # Renderiza el template del informe con los datos obtenidos
        return render(request, 'reporteIngresos.html', {'entradaAlmacenes': entradaAlmacenes})
