from django.db import models
from datetime import date

class Region(models.Model):
    idRegion = models.AutoField(primary_key=True)
    region = models.CharField(max_length=45)

    def __str__(self):
        return self.region

class Marca(models.Model):
    idMarca = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=45)

    def __str__(self):
        return self.marca

class TipoMovimiento(models.Model):
    idTipoMovimiento = models.AutoField(primary_key=True)
    tipoMovimiento = models.CharField(max_length=50)

    def __str__(self):
        return self.tipoMovimiento

class Embalaje(models.Model):
    idEmbalaje = models.AutoField(primary_key=True)
    embalaje = models.CharField(max_length=45)

    def __str__(self):
        return self.embalaje

class UnidadMedida(models.Model):
    idUnidadMedida = models.AutoField(primary_key=True)
    unidadMedida = models.CharField(max_length=50)

    def __str__(self):
        return self.unidadMedida

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria


class TipoProducto(models.Model):
    idTipoProducto = models.AutoField(primary_key=True)
    tipoProducto = models.CharField(max_length=50)

    def __str__(self):
        return self.tipoProducto

class Provincia(models.Model):
    idProvincia = models.AutoField(primary_key=True)
    provincia = models.CharField(max_length=50)
    region_regionId = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.provincia

class Comuna(models.Model):
    idcomuna = models.AutoField(primary_key=True)
    comuna = models.CharField(max_length=50)
    provincia_provinciaId = models.ForeignKey('Provincia', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.comuna

class Proveedor(models.Model):
    rut = models.CharField(max_length=13, primary_key=True)
    nombre = models.CharField(max_length=50)
    fono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    comuna_comunaId = models.ForeignKey('Comuna', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.rut)+ "  -  "+self.nombre

class Modelo(models.Model):
    idModelo = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=50)
    marca_marcaId = models.ForeignKey('Marca', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.modelo

class Movimiento(models.Model):
    codigoMovimiento = models.AutoField(primary_key=True)
    fechaSalida = models.DateField()
    fechaIngreso = models.DateField()
    cantidad = models.IntegerField()
    tipoMovimiento_tipoMovimientoId = models.ForeignKey('TipoMovimiento', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.codigoMovimiento)

class Producto(models.Model):
    codigoProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=15 ,decimal_places=2)
    fechaVencimiento = models.DateField( null=True, blank=True)
    movimiento_codigoMovimiento = models.ForeignKey('Movimiento', on_delete=models.SET_NULL, null=True)
    proveedor_rutProveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True)
    categoria_categoriaId = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    unidadMedida_unidadMedidaId = models.ForeignKey('UnidadMedida', on_delete=models.SET_NULL, null=True)
    tipoProducto_tipoProductoId = models.ForeignKey('TipoProducto', on_delete=models.SET_NULL, null=True)
    modelo_modeloId = models.ForeignKey('Modelo', on_delete=models.SET_NULL, null=True)
    embalaje_embalajeId = models.ForeignKey('Embalaje', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return str(self.codigoProducto) + self.nombre + "| "+str(self.precio)

class Rol(models.Model):
    idRol = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return self.rol


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombreCompleto = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    rol_rolId = models.ForeignKey('Rol', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.idUsuario)+ "| "+self.usuario



