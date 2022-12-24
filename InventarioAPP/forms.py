from django import forms
from .models import * 

from django.contrib.admin.widgets import  AdminDateWidget

class LoginForm(forms.ModelForm):
    required_css_class = 'item-form'
    class Meta:
        model = Usuario
        fields = ['usuario', 'password']

        widgets = {
            'usuario': forms.TextInput(attrs={"class": "form-input", "id":"usuario", "name":"usuario"}),
            'password': forms.PasswordInput(attrs={"class": "form-input", "id":"contrasena", "name":"contrasena"}),
        }

class ProductoForm(forms.ModelForm):
    movimiento_codigoMovimiento = forms.ModelChoiceField(queryset=Movimiento.objects.all(),label="Movimiento", widget=forms.Select(attrs={"class": "form-select form-c1", "id":"movimiento","name":"movimiento"}))
    proveedor_rutProveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(),label="Proovedor", widget=forms.Select(attrs={"class": "form-select form-c1", "id":"proveedor","name":"proveedor"}))
    categoria_categoriaId = forms.ModelChoiceField(queryset=Categoria.objects.all(), label="Categoria",widget=forms.Select(attrs={"class": "form-select form-c1", "id":"categoria","name":"categoria"}))
    unidadMedida_unidadMedidaId = forms.ModelChoiceField(queryset=UnidadMedida.objects.all(),label="Unidad de Medida", widget=forms.Select(attrs={"class": "form-select form-c1", "id":"unidadMedida","name":"unidadMedida"}))
    tipoProducto_tipoProductoId = forms.ModelChoiceField(queryset=TipoProducto.objects.all(),label="Tipo de Producto", widget=forms.Select(attrs={"class": "form-select form-c2", "id":"tipoProd","name":"tipoProd"}))
    modelo_modeloId = forms.ModelChoiceField(queryset=Modelo.objects.all(),label="Modelo", widget=forms.Select(attrs={"class": "form-select form-c2", "id":"modelo","name":"modelo"}))
    embalaje_embalajeId = forms.ModelChoiceField(queryset=Embalaje.objects.all(),label="Embalaje", widget=forms.Select(attrs={"class": "form-select form-c2", "id":"Embalaje","name":"Embalaje"}))
    class Meta:
        model = Producto
        fields = '__all__'

        label = {
            'proveedor_rutProveedor' : 'Proveedor'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={"class": "form-input", "id":"nombre","name":"nombre"}),
            'precio': forms.NumberInput(attrs={"class": "form-input", "id":"precio", "name":"precio"}),
            'fechaVencimiento': AdminDateWidget(attrs={'type': 'date',"id":"fechaVec","name":"fechaVec"})
            #'fechaVencimiento': forms.TextInput(attrs={"class": "form-input", "id":"fechaVec","name":"fechaVec"}),
        
        }