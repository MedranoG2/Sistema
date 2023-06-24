
from django import forms
from django.utils.translation import activate, get_language
from .models import Producto, Proveedor, Departamento, Empleado, Almacen, EntradaAlmacen, Pedido
from datetime import date
from django import forms


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['idProveedor', 'nombre', 'direccion', 'telefono']
        widgets = {
            'idProveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['idDepartamento', 'nombre']
        widgets = {
            'idDepartamento': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['sku', 'nombre', 'precio', 'codigoBarras', 'fkproveedor']
        widgets = {
            'fkproveedor': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Reemplaza 'Proveedor' con tu modelo de proveedor
        self.fields['fkproveedor'].queryset = Proveedor.objects.all()
        self.fields['fkproveedor'].label_from_instance = lambda obj: obj.nombre


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['idEmpleado', 'nombre', 'apellidos', 'fkdepartamento']
        widgets = {
            'fkdepartamento': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Reemplaza 'Proveedor' con tu modelo de proveedor
        self.fields['fkdepartamento'].queryset = Departamento.objects.all()
        self.fields['fkdepartamento'].label_from_instance = lambda obj: obj.nombre


class AlmacenForm(forms.ModelForm):
    codigoBarras = forms.CharField(
        label='Codigo de Barras',
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
    )

    nombreFksu = forms.CharField(
        label='Nombre del Producto',
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = Almacen
        fields = ['Fksku', 'cantidad']
        widgets = {
            'Fksku': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AlmacenForm, self).__init__(*args, **kwargs)
        self.fields['Fksku'].queryset = Producto.objects.all()
        self.fields['Fksku'].label = 'Fksku'
        self.fields['Fksku'].widget.attrs['class'] = 'form-control'


class EntradaAlmacenForm(forms.ModelForm):
    codigoBarras = forms.CharField(
        label='Codigo de Barras',
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
    )
    nombreFksu = forms.CharField(
        label='Nombre del Producto',
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = EntradaAlmacen
        fields = ['Fksku', 'fechaEntrada', 'cantidad']
        widgets = {
            'Fksku': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaEntrada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'},
                                            format='%Y-%m-%d',
                                            ),
        }

    def __init__(self, *args, **kwargs):
        language = get_language()
        activate('es')  # Activa el idioma español
        super(EntradaAlmacenForm, self).__init__(*args, **kwargs)
        self.fields['Fksku'].queryset = Producto.objects.all()
        self.fields['Fksku'].label = 'Fksku'
        self.fields['Fksku'].widget.attrs['class'] = 'form-control'
        self.fields['fechaEntrada'].initial = date.today()


class PedidoForm(forms.ModelForm):
    codigoBarras = forms.CharField(
        label='Codigo de Barras',
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
    )
    nombreFksu = forms.CharField(
        label='Nombre del Producto',
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = Pedido
        fields = ['nombreFksu', 'idEmpleado',
                  'Fksku', 'fechaPedido', 'cantidad']
        widgets = {
            'Fksku': forms.TextInput(attrs={'class': 'form-control fksku-input'}),
            'idEmpleado': forms.TextInput(attrs={'class': 'form-control fksku-input'}),
            'fechaPedido': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'},
                                           format='%Y-%m-%d',
                                           ),
        }

    def __init__(self, *args, **kwargs):
        language = get_language()
        activate('es')  # Activa el idioma español
        super(PedidoForm, self).__init__(*args, **kwargs)
        self.fields['Fksku'].queryset = Producto.objects.all()
        self.fields['Fksku'].label = 'Fksku'
        self.fields['Fksku'].widget.attrs['class'] = 'form-control'
        self.fields['fechaPedido'].initial = date.today()


class BuscarForm(forms.Form):
    buscar = forms.CharField(label='Buscar', required=False, max_length=100)


class BuscarProveedoresForm(forms.Form):
    buscar = forms.CharField(label='Buscar', required=False, max_length=100)


class BuscarProductosForm(forms.Form):
    buscar = forms.CharField(label='Buscar', required=False, max_length=100)
