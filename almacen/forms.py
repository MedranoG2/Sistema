
from django import forms
from django.utils.translation import activate, get_language
from .models import Producto, Proveedor, Departamento, Empleado, Almacen, EntradaAlmacen, Pedido


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
        fields = ['sku', 'nombre', 'precio', 'fkproveedor']
        widgets = {
            'fkproveedor': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Reemplaza 'Proveedor' con tu modelo de proveedor
        self.fields['fkproveedor'].queryset = Proveedor.objects.all()
        self.fields['fkproveedor'].label_from_instance = lambda obj: obj.nombre


class EmpladoForm(forms.ModelForm):
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
    nombreFksu = forms.CharField(
        label='Nombre del Producto',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'readonly': 'readonly'})
    )

    class Meta:
        model = Almacen
        # Lo que hare aqui es Fksku Pasarlo como Producto.Nombre
        fields = ['Fksku', 'cantidad']
        widgets = {
            'Fksku': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AlmacenForm, self).__init__(*args, **kwargs)
        self.fields['Fksku'].queryset = Producto.objects.all()
        self.fields['Fksku'].label = 'Nombre del Producto'
        self.fields['Fksku'].widget.attrs['class'] = 'form-control btn-select'


class EntradaAlmacenForm(forms.ModelForm):
    nombreProductoB = forms.ModelChoiceField(
        queryset=Producto.objects.all(), label='Nombre del Producto',
        widget=forms.Select(attrs={'class': 'form-control btn-select'})
    )

    class Meta:
        model = EntradaAlmacen
        fields = ['nombreProductoB', 'Fksku', 'fechaEntrada', 'cantidad']
        widgets = {
            'Fksku': forms.TextInput(attrs={'class': 'form-control fksku-input', 'readonly': 'readonly'}),
            'fechaEntrada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'},
                                            format='%Y-%m-%d',
                                            ),
        }

    def __init__(self, *args, **kwargs):
        language = get_language()
        activate('es')  # Activa el idioma español
        super(EntradaAlmacenForm, self).__init__(*args, **kwargs)
        self.fields['nombreProductoB'].widget.attrs['class'] = 'form-control btn-select'


class PedidoForm(forms.ModelForm):
    nombreProductoB = forms.ModelChoiceField(
        queryset=Producto.objects.all(), label='Nombre del Producto',
        widget=forms.Select(attrs={'class': 'form-control btn-select'})
    )

    class Meta:
        model = Pedido
        fields = ['nombreProductoB', 'idEmpleado',
                  'Fksku', 'fechaPedido', 'cantidad']
        widgets = {
            'Fksku': forms.TextInput(attrs={'class': 'form-control fksku-input', 'readonly': 'readonly'}),
            'fechaPedido': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'},
                                           format='%Y-%m-%d',
                                           ),
        }

    def __init__(self, *args, **kwargs):
        language = get_language()
        activate('es')  # Activa el idioma español
        super(PedidoForm, self).__init__(*args, **kwargs)
        self.fields['nombreProductoB'].widget.attrs['class'] = 'form-control btn-select'
