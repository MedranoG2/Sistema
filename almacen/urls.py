from django.urls import path
from . import views
from .views import GenerarReporteIngresoView, ReporteExcel, GenerarReportePedidosView, ReporteExcelPedidos


urlpatterns = [


    path('inicio/', views.inicio, name='inicio'),
    path('registroProveedor/', views.registrarProveedor,
         name='registrar_proveedor'),

    path('edicionProveedor/<codigo>/',
         views.edicionProveedor, name='edicion_proveedor'),

    path('actualizarProveedor/<codigo>/',
         views.actualizar_proveedor, name='actualizar_proveedor'),

    path('eliminarProveedor/<codigo>/',
         views.eliminarProveedor, name='eliminar_proveedor'),

    path('registroProducto/', views.registrarProducto, name='registrar_producto'),
    path('eliminarProducto/<codigo>/',
         views.eliminarProducto, name='eliminar_producto'),
    path('edicionProducto/<codigo>/',
         views.edicionProducto, name='edicion_producto'),
    path('actualizarProducto/<codigo>/',
         views.actualizarProducto, name='actualizar_producto'),

    path('registroDepartamento/', views.registrarDepartamento,
         name='registroDepartamento'),

    path('edicionDepartamento/<codigo>/',
         views.edicionDepartamento, name='edicion_departamento'),
    path('actualizarDepartamento/<codigo>/',
         views.actualizarDepartamento, name='actualizar_departamento'),
    path('eliminarDepartamento/<codigo>/',
         views.eliminarDepartamento, name='eliminar_departamento'),


    path('registroEmpleado/', views.registrarEmpleado,
         name='registroEmpleado'),
    path('edicionEmpleado/<codigo>/',
         views.edicionEmpleado, name='edicion_empleado'),
    path('actualizarEmpleado/<codigo>/',
         views.actualizarEmpleado, name='actualizar_empleado'),
    path('eliminarEmpleado/<codigo>/',
         views.eliminarEmpleado, name='eliminar_Empleado'),

    path('registroAlmacen/', views.registrarAlmacen,
         name='registrar_almacen'),

    path('edicionAlmacen/<codigo>/',
         views.edicionAlmacen, name='edicion_almacen'),

    path('actualizarAlmacen/<codigo>/',
         views.actualizarAlmacen, name='actualizar_almacen'),
    path('eliminarAlmacen/<codigo>/',
         views.eliminarAlmacen, name='eliminar_Almacen'),

    path('registroEntradaAlmacen/', views.registrarEntradaAlmacen,
         name='registrar_EntradaAlmacen'),

    path('edicionEntradaAlmacen/<codigo>/',
         views.edicionEntradaAlmacen, name='edicion_EntradaAlmacen'),

    path('actualizarEntradaAlmacen/<codigo>/',
         views.actualizarEntradaAlmacen, name='actualizar_EntradaAlmacen'),
    path('eliminarEntradaAlmacen/<codigo>/',
         views.eliminarEntradaAlmacen, name='eliminar_EntradaAlmacen'),

    path('registroPedido/', views.registrarPedido,
         name='registrar_Pedido'),

    path('edicionPedido/<codigo>/',
         views.edicionPedido, name='edicion_pedido'),

    path('actualizarPedido/<codigo>/',
         views.actualizarPedido, name='actualizar_pedido'),

    path('eliminarPedido/<codigo>/',
         views.eliminarPedido, name='eliminar_pedido'),


    path('reportePedido/', views.reportePedido, name='reportePedido'),
    path('reporteIngresos/', views.reporteIngresos, name='reporteIngresos'),

    path('generar_reporte_ingresos', GenerarReporteIngresoView.as_view(),
         name='generar_reporte_ingresos'),
    path('generar_excel/', ReporteExcel.as_view(),
         name='generar_excel'),


    path('generar_reporte_pedidos', GenerarReportePedidosView.as_view(),
         name='generar_reporte_pedidos'),
    path('generar_excel_pedidos/', ReporteExcelPedidos.as_view(),
         name='generar_excel_pedidos'),
    path('graficoPedido/', views.graficoPedido, name='graficoPedido'),
    path('graficoIngreso/', views.graficoIngreso, name='graficoIngreso'),

]
