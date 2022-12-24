from django.contrib import admin
from .models import *

@admin.register(Rol, Usuario, Region, Provincia, Comuna, Proveedor, Producto, Modelo, Marca, TipoMovimiento, TipoProducto, Movimiento, Categoria, UnidadMedida, Embalaje)
class DefaultAdmin(admin.ModelAdmin):
    pass