from django.shortcuts import render, redirect
from .models import Proveedor, Producto, Departamento, Empleado, Almacen, EntradaAlmacen, Pedido
from django.contrib import messages
from .forms import ProductoForm, ProveedorForm, DepartamentoForm, EmpladoForm, AlmacenForm, EntradaAlmacenForm, PedidoForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import View
from django.db.models import Q
from openpyxl import Workbook
from django.http import HttpResponse


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


class GenerarReportePedidosView(View):
    def post(self, request):
        context = {}
        fecha_inicio = request.POST.get(
            'fecha_inicio') if request.POST.get('fecha_inicio') else ''
        fecha_fin = request.POST.get(
            'fecha_fin') if request.POST.get('fecha_fin') else ''
        nombre_producto = request.POST.get(
            'nombre_producto') if request.POST.get('nombre_producto') else ''
        fksku = request.POST.get('fksku') if request.POST.get('fksku') else ''

        context['fecha_inicio'] = fecha_inicio
        context['fecha_fin'] = fecha_fin
        context['nombre_producto'] = nombre_producto
        context['fksku'] = fksku

        pedidos = Pedido.objects.filter(
            fechaPedido__range=[fecha_inicio, fecha_fin],
            Fksku__nombre__icontains=nombre_producto,
            Fksku__sku__icontains=fksku
        )
        context['pedidos'] = pedidos
        return render(request, 'reportePedido.html', context)


class ReporteExcelPedidos(View):
    def get(self, request):
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_fin = request.GET.get('fecha_fin')

        nombre_producto = request.GET.get('nombre_producto')
        fksku = request.GET.get('fksku')

        pedidos = Pedido.objects.filter(
            Q(fechaPedido__range=[fecha_inicio, fecha_fin]),
            Q(Fksku__sku__icontains=fksku),
            Q(Fksku__nombre__icontains=nombre_producto))

        wb = Workbook()
        ws = wb.active
        ws['B1'] = "REPORTE DE PEDIDOS"

        ws.merge_cells("B1:E1")
        ws['B3'] = 'ID Entrada'
        ws['C3'] = 'Nombre del Producto'
        ws['D3'] = 'FK Sku'
        ws['E3'] = 'Fecha de Ingreso'
        ws['F3'] = 'Cantidad'
        ws['G3'] = 'Precio Unitario'
        ws['H3'] = 'Valor Total'

        cont = 4
        for x in pedidos:
            ws.cell(row=cont, column=2).value = x.idPedido
            ws.cell(row=cont,  column=3).value = x.Fksku.nombre
            ws.cell(row=cont, column=4).value = x.Fksku.sku
            ws.cell(row=cont, column=5).value = x.fechaPedido
            ws.cell(row=cont, column=6).value = x.cantidad
            ws.cell(row=cont, column=7).value = x.Fksku.precio
            ws.cell(row=cont, column=8).value = x.cantidad * x.Fksku.precio
            cont += 1

        response = HttpResponse(content_type="application/ms-excel")
        content = "attachment; filename=Reporte-Pedidos.xlsx"
        response['Content-Disposition'] = content
        wb.save(response)
        return response


class GenerarReporteIngresoView(View):
    def post(self, request):
        context = {}
        fecha_inicio = request.POST.get(
            'fecha_inicio') if request.POST.get('fecha_inicio') else ''
        fecha_fin = request.POST.get(
            'fecha_fin') if request.POST.get('fecha_fin') else ''
        nombre_producto = request.POST.get(
            'nombre_producto') if request.POST.get('nombre_producto') else ''
        fksku = request.POST.get('fksku') if request.POST.get('fksku') else ''

        context['fecha_inicio'] = fecha_inicio
        context['fecha_fin'] = fecha_fin
        context['nombre_producto'] = nombre_producto
        context['fksku'] = fksku

        entradaAlmacenes = EntradaAlmacen.objects.filter(
            fechaEntrada__range=[fecha_inicio, fecha_fin],
            Fksku__nombre__icontains=nombre_producto,
            Fksku__sku__icontains=fksku
        )
        context['entradaAlmacenes'] = entradaAlmacenes
        return render(request, 'reporteIngresos.html', context)


class ReporteExcel(View):
    def get(self, request):
        fecha_inicio = request.GET.get('fecha_inicio')
        fecha_fin = request.GET.get('fecha_fin')

        nombre_producto = request.GET.get('nombre_producto')
        fksku = request.GET.get('fksku')

        entradaAlmacenes = EntradaAlmacen.objects.filter(
            Q(fechaEntrada__range=[fecha_inicio, fecha_fin]),
            Q(Fksku__sku__icontains=fksku),
            Q(Fksku__nombre__icontains=nombre_producto))

        wb = Workbook()
        ws = wb.active
        ws['B1'] = "REPORTE DE INGRESOS"

        ws.merge_cells("B1:E1")
        ws['B3'] = 'ID Entrada'
        ws['C3'] = 'Nombre del Producto'
        ws['D3'] = 'FK Sku'
        ws['E3'] = 'Fecha de Ingreso'
        ws['F3'] = 'Cantidad'
        ws['G3'] = 'Precio Unitario'
        ws['H3'] = 'Valor Total'

        cont = 4
        for x in entradaAlmacenes:
            ws.cell(row=cont, column=2).value = x.idEntradaAlmacen
            ws.cell(row=cont,  column=3).value = x.Fksku.nombre
            ws.cell(row=cont, column=4).value = x.Fksku.sku
            ws.cell(row=cont, column=5).value = x.fechaEntrada
            ws.cell(row=cont, column=6).value = x.cantidad
            ws.cell(row=cont, column=7).value = x.Fksku.precio
            ws.cell(row=cont, column=8).value = x.cantidad * x.Fksku.precio
            cont += 1

        response = HttpResponse(content_type="application/ms-excel")
        content = "attachment; filename=Reporte-Ingresos.xlsx"
        response['Content-Disposition'] = content
        wb.save(response)
        return response
