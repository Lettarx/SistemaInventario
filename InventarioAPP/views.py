from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

#LOGIN
def login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = request.POST['usuario']
        password = request.POST['password']
        try:
            usuario = Usuario.objects.get(usuario=user)
        except ObjectDoesNotExist:
            html = '<span>Usuario no existe</span><br><a href="">volver</a>'
            return HttpResponse(html)
        if form.is_valid():
             if usuario:
                if (usuario.usuario == user) and (usuario.password == password):
                    return inicio(request)
        
        
    data = {'formLogin': form}
    return render(request,'Login.html', data)


#INICIO
def inicio(request):
    return render(request, 'Inicio.html')



#MODULO PRODUCTOS
def productos(request):
     prod = Producto.objects.all()
     data = {'productos':prod}
     return render(request,'Productos.html',data)

def addProducto(request):
     form = ProductoForm()
     if request.method == 'POST':
         form = ProductoForm(request.POST)
         if form.is_valid():
             form.save()
         return productos(request)
     data = {'form':form}
     return render(request,'AddProducto.html',data)

def actualizarProducto(request,id):
    prod = Producto.objects.get(codigoProducto = id)
    form = ProductoForm(instance=prod)
    if request.method == 'POST':
        form = ProductoForm(request.POST,instance=prod)
        if form.is_valid():
            form.save()
        return productos(request)
    data = {'form':form}
    return render(request,'AddProducto.html',data)

def eliminarProducto(request,id):
    prod = Producto.objects.get(codigoProducto = id)
    prod.delete()
    return redirect('/productos')



#MODULO CONFIGURACION



#MODULO PROVEEDORES
def proveedores(request):
     prod = Proveedor.objects.all()
     data = {'proveedores':prod}
     return render(request,'Proveedores.html',data)

def addProveedor(request):
     form = ProveedoresForm()
     if request.method == 'POST':
         form = ProveedoresForm(request.POST)
         if form.is_valid():
             form.save()
         return proveedores(request)
     data = {'form':form}
     return render(request,'AddProveedores.html',data)

def actualizarProveedor(request,id):
    prov = Proveedor.objects.get(rut = id)
    form = ProveedoresForm(instance=prov)
    if request.method == 'POST':
        form = ProveedoresForm(request.POST,instance=prov)
        if form.is_valid():
            form.save()
        return proveedores(request)
    data = {'form':form}
    return render(request,'AddProveedores.html',data)

def eliminarProveedor(request,id):
    prov = Proveedor.objects.get(rut = id)
    prov.delete()
    return redirect('/proveedores')


#Configuracion
def config(request):
    return render(request, 'Configuracion.html')


#Salidas



#Entradas